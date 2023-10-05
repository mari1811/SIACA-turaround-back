from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import UsuarioSerializer, UsuarioListaSerializer, DatosSerializer, DatosListaSerializer, IDSerialier, UpdateUserSeralizer, UpdateUsuarioSerializer, UpdateSeralizer, EstadoUsuarioSerializer, IDSolicitudes, UsuarioTurnaroundSerializer, UsuarioDatosTurnaroundSerializer
from api.models import usuario, usuario_turnaround
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta



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
            return Response(usuarios_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(usuarios_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def usuarios_detalles_view(request, pk=None):
    #Consulta de usuario
    user = User.objects.filter(id = pk).first()

    #Validación 
    if user:

        #Buscar un usuario
        if request.method == 'GET':
            usuario_serializer = UsuarioSerializer(user)
            return Response(usuario_serializer.data, status=status.HTTP_200_OK)
        
        #Actualizar datos de un usuario
        elif request.method == 'PUT':
            usuario_serializer = UpdateUserSeralizer(user, data=request.data)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response(usuario_serializer.data, status=status.HTTP_200_OK)
            return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #Eliminar un usuario
        elif request.method == 'DELETE':
            user.delete()
            return Response({'mensaje':'Usuario eliminado'}, status=status.HTTP_200_OK)

    #No existe el usuario   
    return Response({'mensaje':'No se ha encontrado el usuario'}, status=status.HTTP_400_BAD_REQUEST)

class Update(APIView):

    def patch(self, request, pk =None, *args, **kwargs):

        user = User.objects.filter(id = pk).first()
        usuario_serializer = UpdateSeralizer(user, data=request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return Response(usuario_serializer.data, status=status.HTTP_200_OK)
        return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST', 'PUT'])
def datos_api_view(request, pk=None):

    #Lista de uausarios
    if request.method == 'GET':
        datos = usuario.objects.filter(id = pk).first()
        datos_serializer = DatosListaSerializer(datos)
        return Response (datos_serializer.data, status=status.HTTP_200_OK)

class Lista(APIView):

    def get(self, request, *args, **kwargs):
    #Lista de usuarios
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            if request.method == 'GET':
                datos = usuario.objects.filter(fk_user__is_active = True)
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

    def delete(self, request, pk =None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            user = User.objects.filter(id = pk).first()
            if user:
                user.delete()
                return Response({'mensaje':'Usuario eliminada'}, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class EstadoUsuario(APIView):
     
     #Modificar estado de maquinaria
        def patch(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                user = User.objects.filter(id = pk).first()
                if user.is_active == False:
                    usuario_serializer = EstadoUsuarioSerializer(user, data={"is_active": True})
                    if usuario_serializer.is_valid():
                        usuario_serializer.save()
                        return Response(usuario_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No se ha encontrado el usuario'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class Solicitudes(APIView):

    def get(self, request, *args, **kwargs):
    #Lista de solicitudes
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            datos = usuario.objects.filter(fk_user__is_active = False)

            datos_serializer = DatosListaSerializer(datos, many=True)
            return Response (datos_serializer.data, status=status.HTTP_200_OK)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
class Contador(APIView):

    def get(self, request, *args, **kwargs):
    #Contador de solicitudes 
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            contador = usuario.objects.filter(fk_user__is_active = False).count()

            return Response ({"contador":contador}, status=status.HTTP_200_OK)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
class UsuarioHistorial(APIView):
     
    #Asignar hora inicio y fin     
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
    
    #Buscar maquinarias por categoria
    def get(self, request, fecha=None, horaI=None, horaF=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            hourI= datetime.strptime(horaI, '%H:%M')
            hourF= datetime.strptime(horaF, '%H:%M')
            min = timedelta(minutes=10)
            max = timedelta(minutes=60)
            usuarios = usuario_turnaround.objects.filter(fecha = fecha).filter(hora_inicio__range = (hourI , hourF )).all() | usuario_turnaround.objects.filter(fecha = fecha).filter(hora_fin__range = (hourI , hourF )).all()
            if usuarios:
                usuario_serializer = UsuarioTurnaroundSerializer(usuarios, many = True)
                return Response(usuario_serializer.data, status=status.HTTP_200_OK)
            return Response([{}])
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)