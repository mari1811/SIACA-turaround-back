from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import UsuarioSerializer, UsuarioListaSerializer
from api.models import usuario

@api_view(['GET','POST'])
def usuario_api_view(request):

    #Lista de uausarios
    if request.method == 'GET':
        usuarios = usuario.objects.all()
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
    user = usuario.objects.filter(id = pk).first()

    #Validación 
    if user:

        #Buscar un usuario
        if request.method == 'GET':
            usuario_serializer = UsuarioSerializer(user)
            return Response(usuario_serializer.data, status=status.HTTP_200_OK)
        
        #Actualizar datos de un usuario
        elif request.method == 'PUT':
            usuario_serializer = UsuarioSerializer(user, data=request.data)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response(usuario_serializer.data, status=status.HTTP_200_OK)
            return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #Eliminar un usuario
        elif request.method == 'DELETE':
            user.delete()
            return Response({'mensaje':'Usuario eliminado'}, status=status.HTTTP_200_OK)

    #No existe el usuario   
    return Response({'mensaje':'No se ha encontrado el usuario'}, status=status.HTTP_400_BAD_REQUEST)
