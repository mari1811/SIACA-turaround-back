from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import PlantillaSerializer, TareaSerializer, SubtareaSerializer
from api.models import plantilla, tarea, subtarea
from rest_framework import filters
from rest_framework import generics



@api_view(['GET','POST'])
def plantilla_api_view(request):

    #Lista de plantillas
    if request.method == 'GET':
        plantilla = plantilla.objects.all()
        plantilla_serializer = PlantillaSerializer(plantilla, many = True)
        return Response (plantilla_serializer.data, status=status.HTTP_200_OK)
    
    #Crear una plantilla
    elif request.method == 'POST':
        plantilla_serializer = PlantillaSerializer(data = request.data)
        if plantilla_serializer.is_valid():
            plantilla_serializer.save()
            return Response(plantilla_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(plantilla_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def tarea_api_view(request):

    #Crear una tarea
    if request.method == 'POST':
        tarea_serializer = TareaSerializer(data = request.data)
        if tarea_serializer.is_valid():
            tarea_serializer.save()
            return Response(tarea_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(tarea_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def subtarea_api_view(request):

    #Crear una subtarea
    if request.method == 'POST':
        subtarea_serializer = SubtareaSerializer(data = request.data)
        if subtarea_serializer.is_valid():
            subtarea_serializer.save()
            return Response(subtarea_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(subtarea_serializer.errors, status=status.HTTP_400_BAD_REQUEST)