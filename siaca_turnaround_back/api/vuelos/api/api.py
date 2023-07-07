from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import VueloSerializer, ListaVuelosSerializer
from api.models import vuelo
from rest_framework import filters
from rest_framework import generics


@api_view(['GET','POST'])
def vuelo_api_view(request):

    #Lista de vuelos con toda su información
    if request.method == 'GET':
        vuelos = vuelo.objects.all()
        vuelos_serializer = VueloSerializer(vuelos, many = True)
        return Response (vuelos_serializer.data, status=status.HTTP_200_OK)
    
    #Crear un vuelo
    elif request.method == 'POST':
        vuelos_serializer = VueloSerializer(data = request.data)
        if vuelos_serializer.is_valid():
            vuelos_serializer.save()
            return Response(vuelos_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(vuelos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def modificar_api_vuelos(request, pk=None):

    #Consulta de vuelo
    fly = vuelo.objects.filter(id = pk).first()

    #Validación 
    if fly:

        #Buscar un vuelo específico
        if request.method == 'GET':
            vuelo_serializer = ListaVuelosSerializer(fly)
            return Response(vuelo_serializer.data, status=status.HTTP_200_OK)
        
        #Actualizar datos de un vuelo
        elif request.method == 'PUT':
            vuelo_serializer = VueloSerializer(fly, data=request.data)
            if vuelo_serializer.is_valid():
                vuelo_serializer.save()
                return Response(vuelo_serializer.data, status=status.HTTP_200_OK)
            return Response(vuelo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #Eliminar un vuelo
        elif request.method == 'DELETE':
            fly.delete()
            return Response({'mensaje':'Vuelo eliminado'}, status=status.HTTP_200_OK)

    #No existe el vuelo   
    return Response({'mensaje':'No se ha encontrado el vuelo'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def lista_api_vuelo(request):

    #Lista de vuelos vista principal
    if request.method == 'GET':
        vuelos = vuelo.objects.all()
        vuelos_serializer = ListaVuelosSerializer(vuelos, many = True)
        return Response (vuelos_serializer.data, status=status.HTTP_200_OK)


