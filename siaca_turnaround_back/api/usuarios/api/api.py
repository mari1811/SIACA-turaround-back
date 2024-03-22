from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import UsuarioSerializer, UsuarioListaSerializer, DatosSerializer, DatosListaSerializer, IDSerialier, UpdateUsuarioSerializer, UpdateSeralizer
from .serializer import EstadoUsuarioSerializer, UsuarioTurnaroundSerializer, UsuarioDatosTurnaroundSerializer, CargoSerializer, DepartamentoSerializer, DepartamentoUsuarioListaSerializer
from api.models import usuario, usuario_turnaround, departamento, cargo
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta
from django.db.models import Count, Sum, F, Value, Func, CharField
from django.db.models.functions import Concat
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from django.db.models import Q



@api_view(['GET','POST'])
def usuario_api_view(request):

    #Lista de uausarios
    if request.method == 'GET':
        usuarios = User.objects.all()
        usuarios_serializer = UsuarioListaSerializer(usuarios, many = True)
        return Response (usuarios_serializer.data, status=status.HTTP_200_OK)
    
    #Crear un usuario
    elif request.method == 'POST':
        usuarios_serializer = UsuarioSerializer(data = request.data)
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
            #Envía un correo al administradore para informar que hay nuevas solicitudes de usuario
            msg = EmailMultiAlternatives(
            'Nueva solicitud de usuario',
            'Tiene una nueva solicitud de usuario en el sistema de SIACA\n',
            settings.EMAIL_HOST_USER,
            #Correo del administrador
            ["."]
        )
            msg.send()
            return Response(usuarios_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(usuarios_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Departamento(APIView):

    #Lista de departamentos
    def get(self, request, *args, **kwargs):
        
            if request.method == 'GET':
                datos = departamento.objects.all()
                datos_serializer = DepartamentoSerializer(datos, many = True)
                return Response (datos_serializer.data, status=status.HTTP_200_OK)
            
class Cargo(APIView):

    #Lista de cargos 
    def get(self, request, *args, **kwargs):
        
            if request.method == 'GET':
                datos = cargo.objects.all()
                datos_serializer = CargoSerializer(datos, many = True)
                return Response (datos_serializer.data, status=status.HTTP_200_OK)
    

class Update(APIView):

    #Editar usuario
    def patch(self, request, pk =None, *args, **kwargs):

        user = User.objects.filter(id = pk).first()
        usuario_serializer = UpdateSeralizer(user, data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data, status=status.HTTP_200_OK)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Lista(APIView):

    def get(self, request, *args, **kwargs):
    #Lista de usuarios
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            if request.method == 'GET':
                datos = usuario.objects.filter(fk_user__is_active = True).order_by("fk_departamento__nombre").all()
                datos_serializer = DatosListaSerializer(datos, many = True)
                return Response (datos_serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def registro_usuario(request):

    #Crear un usuario
    if request.method == 'POST':
        datos_serializer = UpdateUsuarioSerializer(data = request.data)
        if datos_serializer.is_valid():
            datos_serializer.save()
            return Response(datos_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(datos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Buscar usuario por username 
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = IDSerialier
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


class Prueba(APIView):

    def get(self, request, *args, **kwargs):
        
            if request.method == 'GET':
                datos = User.objects.all()
                datos_serializer = UsuarioListaSerializer(datos, many = True)
                return Response (datos_serializer.data, status=status.HTTP_200_OK)
            
class DeleteUser(APIView):

    #Eliminar usuario
    def delete(self, request, pk =None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            user = User.objects.filter(id = pk).first()
            if user:
                user.delete()
                #Envía un correo al usuario para informar que su usuario fue rechazado o eliminar 
                msg = EmailMultiAlternatives(
                'Solicitud de usuario eliminado',
                'Su usuario ha sido RECHAZADO o ELIMINADO del sistema de SIACA, comuniquese con el administrador para solucionar el problema\n',
                settings.EMAIL_HOST_USER,
                [user.username]
                )
                msg.send()
                return Response({'mensaje':'Usuario eliminada'}, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class EstadoUsuario(APIView):
     
     #MCambiar estado de usuario (activo/no activo)
        def patch(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                user = User.objects.filter(id = pk).first()
                if user.is_active == False:
                    usuario_serializer = EstadoUsuarioSerializer(user, data={"is_active": True})
                    if usuario_serializer.is_valid():
                        usuario_serializer.save()
                        #Envía un correo al usuario para informar que su usuario fue acepptado
                        msg = EmailMultiAlternatives(
                        'Solicitud de usuario aceptada',
                        'Su usuario ya esta ACTIVO, puede ingresar al sistema de SIACA\n',
                        settings.EMAIL_HOST_USER,
                        [user.username]
                        )
                        msg.send()
                        return Response(usuario_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No se ha encontrado el usuario'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class Solicitudes(APIView):

    #Lista de solicitudes de usuarios
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            datos = usuario.objects.filter(fk_user__is_active = False)

            datos_serializer = DatosListaSerializer(datos, many=True)
            return Response (datos_serializer.data, status=status.HTTP_200_OK)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
class Contador(APIView):

    def get(self, request, *args, **kwargs):
    #Contador de solicitudes de usuario
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            contador = usuario.objects.filter(fk_user__is_active = False).count()

            return Response ({"contador":contador}, status=status.HTTP_200_OK)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
class UsuarioHistorial(APIView):
     
    #Asignar personal a turnaround   
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                usuario_serializer = UsuarioDatosTurnaroundSerializer(data = request.data)
                if usuario_serializer.is_valid():
                    usuario_serializer.save()
                    return Response(usuario_serializer.data, status=status.HTTP_201_CREATED)
                return Response({'mensaje':'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    #Lista de perosnal disponible
    def get(self, request, fecha=None, horaI=None, horaF=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            hourI= datetime.strptime(horaI, '%H:%M')
            hourF= datetime.strptime(horaF, '%H:%M')
            min = timedelta(minutes=10)
            max = timedelta(minutes=60)
            usuarios = usuario_turnaround.objects.filter(
                    Q(fecha=fecha) &
                    (Q(hora_inicio__gte=hourI, hora_inicio__lte=hourF) |
                    Q(hora_fin__gte=hourI, hora_fin__lte=hourF) |
                    Q(hora_inicio__lte=hourI, hora_fin__gte=hourF))
                ).all()
            if usuarios:
                usuario_serializer = UsuarioTurnaroundSerializer(usuarios, many = True)
                return Response(usuario_serializer.data, status=status.HTTP_200_OK)
            return Response([{}])
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class MetricaTurnaroundPersonal(APIView):
        
        #Metrica de personal
        def get(self, request, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                usuarios = usuario_turnaround.objects.values( 'fk_usuario__id','fk_usuario__departamento')
                contador = usuarios.annotate(contador=Count('fk_usuario__id')).filter(contador__gt=0).annotate(full_name=Concat('fk_usuario__fk_user__first_name', Value(' '), 'fk_usuario__fk_user__last_name',  output_field=CharField()))
                if usuarios:
                    return Response(contador , status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay maquinarias en esta categoria'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class UsuarioTurnaround(APIView):
        
        #Lista de personal asignado a turnaround
        def get(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                usuarios = usuario_turnaround.objects.filter(fk_turnaround__id = pk).order_by("fk_usuario_id").all()
                if usuarios:
                    usuario_serializer = DepartamentoUsuarioListaSerializer(usuarios,  many = True)
                    return Response(usuario_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay maquinarias asignadas para este turnaround'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class CorreoLista(APIView):
        
        #Correo con la lista del personal asignado a un Turnaround
        def get(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key=token).first()
            if token:
                usuarios = usuario_turnaround.objects.filter(fk_turnaround__id=pk).order_by("fk_usuario_id").all()
                if usuarios:
                    usuario_serializer = UsuarioTurnaroundSerializer(usuarios, many=True)
                    user_data = []
                    for user in usuario_serializer.data:
                        user_data.append({
                            'first_name': user['fk_usuario']['fk_user']['first_name'],
                            'last_name': user['fk_usuario']['fk_user']['last_name'],
                            'username': user['fk_usuario']['fk_user']['username'],
                            'cedula': user['fk_usuario']['cedula']
                        })
                    msg = EmailMultiAlternatives(
                        'Lista de personal turnaround ' + ' ' + f'{usuario_serializer.data[0]["fecha"]}',
                        'Se realizó la asignación de personal al siguiente Turnaround:'
                        '\n\nID Turnaround: '+ f'{usuario_serializer.data[0]["fk_turnaround"]["id"]}'
                        '\nNo. vuelo: '+ f'{usuario_serializer.data[0]["fk_turnaround"]["fk_vuelo"]["numero_vuelo"]}' +
                        '\nAerolinea: '+ f'{usuario_serializer.data[0]["fk_turnaround"]["fk_vuelo"]["fk_aerolinea"]["nombre"]}'+
                        '\n\nLista de personal:\n' + '\n'.join([f"{user['first_name']}, {user['last_name']} - {user['cedula']} - {user['username']}" for user in user_data]) + 
                        f'\n\nFecha: {usuario_serializer.data[0]["fecha"]}\nHora de inicio: {usuario_serializer.data[0]["hora_inicio"]}\nHora de fin: {usuario_serializer.data[0]["hora_fin"]}\n',
                        settings.EMAIL_HOST_USER,
                        ["correo@gmail.com"],
                    )
                    msg.send()
                    return Response(user_data, status=status.HTTP_200_OK)
                return Response({'mensaje': 'No hay personal asignado para este turnaround'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje': 'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        


class ListaFiltro(APIView):

    def get(self, request, *args, **kwargs):
        #Lista de usuarios
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            if request.method == 'GET':
                usuarios = usuario.objects.filter(
                Q(fk_departamento__nombre="Operaciones") |
                Q(fk_departamento__nombre="Mantenimiento") |
                Q(fk_departamento__nombre="Servicio al Pasajero") |
                Q(fk_departamento__nombre="Despacho de Vuelos") |
                Q(fk_departamento__nombre="Seguridad Operacional") |
                Q(fk_departamento__nombre="Servicios Especiales")
                ).all()
                datos_serializer = DatosListaSerializer(usuarios, many = True)
                return Response (datos_serializer.data, status=status.HTTP_200_OK)
            

class ListaFiltroDepartamento(APIView):

    def get(self, request, *args, **kwargs):
        #Lista de usuarios
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            if request.method == 'GET':
                departamentos = departamento.objects.filter(
                Q(nombre="Operaciones") |
                Q(nombre="Mantenimiento") |
                Q(nombre="Servicio al Pasajero") |
                Q(nombre="Despacho de Vuelos") |
                Q(nombre="Seguridad Operacional") |
                Q(nombre="Servicios Especiales")
                ).all()
                datos_serializer = DepartamentoSerializer(departamentos, many = True)
                return Response (datos_serializer.data, status=status.HTTP_200_OK)
