from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import PlantillaSerializer, TareaSerializer, SubtareaSerializer, TareaVistaSerializer, SubareaVistaSerializer, CantidadSerializer, CategoriaSerializer, PlantillaMaquinariaSerializer, TipoSerializer
from api.models import plantilla, tarea, subtarea, cantidad_categoria, categoria, tipo
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token


class Plantilla(APIView):

    #Lista de plantillas
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                plantillas = plantilla.objects.all()
                plantillas_serializer = PlantillaSerializer(plantillas, many = True)
                return Response (plantillas_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
   
    #Crear una Plantilla      
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                plantilla_serializer = PlantillaSerializer(data = request.data)
                if plantilla_serializer.is_valid():
                    plantilla_serializer.save()
                    return Response(plantilla_serializer.data, status=status.HTTP_201_CREATED)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class Tarea(APIView):

    #Crear una tarea
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                tarea_serializer = TareaSerializer(data = request.data)
                if tarea_serializer.is_valid():
                    tarea_serializer.save()
                    return Response(tarea_serializer.data, status=status.HTTP_201_CREATED)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class Subtarea(APIView):

    #Crear una subtarea
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                subtarea_serializer = SubtareaSerializer(data = request.data)
                if subtarea_serializer.is_valid():
                    subtarea_serializer.save()
                    return Response(subtarea_serializer.data, status=status.HTTP_201_CREATED)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
class Maquinaria(APIView):
    
    def post(self, request, *args, **kwargs):
        
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            maquinaria_serializer = CantidadSerializer(data = request.data)
            if maquinaria_serializer.is_valid():
                maquinaria_serializer.save()
                return Response(maquinaria_serializer.data, status=status.HTTP_201_CREATED)
                
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class Categoria(APIView):


    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinarias = categoria.objects.all()
                maquinaria_serializer = CategoriaSerializer(maquinarias, many = True)
                return Response (maquinaria_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                categoria_serializer = CategoriaSerializer(data = request.data)
                if categoria_serializer.is_valid():
                    categoria_serializer.save()
                    return Response(categoria_serializer.data, status=status.HTTP_201_CREATED)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
class Tipo(APIView):


    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                tipos = tipo.objects.all()
                tipo_serializer = TipoSerializer(tipos, many = True)
                return Response (tipo_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)


class VistaPlantilla(APIView):
    
    #Buscar una plantilla con sus detalles 
    def get(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            detalles = tarea.objects.filter(fk_plantilla_id = pk)
            if detalles:
                plantilla_serializer = TareaVistaSerializer(detalles, many = True)
                return Response(plantilla_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado la plantilla'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    #Buscar una plantilla con sus detalles 
    def delete(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            detalles = plantilla.objects.filter(id = pk)
            tareas = tarea.objects.filter(fk_plantilla = pk)
            if detalles:
                detalles.delete()
                tareas.delete()
                return Response({'mensaje':'Plantilla eliminada'}, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado la plantilla'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)

class VistaSubtarea(APIView):
     
     def get(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            detalles = subtarea.objects.filter(fk_tarea_id = pk)
            if detalles:
                plantilla_serializer =SubareaVistaSerializer(detalles, many = True)
                return Response(plantilla_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado la plantilla'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
     

class VistaMaquinaria(APIView):
     
    def get(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            detalles = cantidad_categoria.objects.filter(fk_plantilla_id = pk)
            if detalles:
                plantilla_serializer = PlantillaMaquinariaSerializer(detalles, many = True)
                return Response(plantilla_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado la plantilla'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)

