from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import UsuarioSerializer, UsuarioListaSerializer, DatosSerializer, DatosListaSerializer, IDSerialier, UpdateUserSeralizer, UpdateUsuarioSerializer, UpdateSeralizer
from api.models import usuario
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token



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
                datos = usuario.objects.all()
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