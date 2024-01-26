from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import PlantillaSerializer, TareaSerializer, SubtareaSerializer, TareaVistaSerializer, SubareaVistaSerializer, CantidadSerializer, CategoriaSerializer
from .serializer import PlantillaMaquinariaSerializer, TipoSerializer, PlantillaTareaSubtareaSerializer
from api.models import plantilla, tarea, subtarea, cantidad_categoria, categoria, tipo, tipo_subtarea, Hora
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.db.models import F, Q
from django.http import JsonResponse
from django.db import connection



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
    
    #Agregar la cantidad de maquinarias 
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

    #Lista de categorias
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinarias = categoria.objects.all()
                maquinaria_serializer = CategoriaSerializer(maquinarias, many = True)
                return Response (maquinaria_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    #Agregar nueva categoria
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

    #Lista de tipos de subtareas
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
    
    #Eliminar plantilla
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
     
     #Plantilla con todas sus tareas y subtareas por ID
     def get(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            detalles = subtarea.objects.filter(fk_tarea__fk_plantilla_id = pk)
            if detalles:
                plantilla_serializer = SubareaVistaSerializer(detalles, many = True)
                return Response(plantilla_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado la plantilla'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
     

class VistaMaquinaria(APIView):
     
     #Cantidad de maquinarias necesarias por plantilla especifica por ID
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


class ContadorMaquinaria(APIView):
     
     #Contador del numeor de categorias
     def get (self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
             maquinarias = categoria.objects.all().count()
             return Response ({"contador": maquinarias}, status=status.HTTP_200_OK)

        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)


class Plantillas(APIView):
     
     #Lista de todas las plantillas con todas sus tareas y subtareas
     def get (self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            result = subtarea.objects.filter(fk_tarea__fk_plantilla__titulo = "PLANTILLA DE PRUEBA").filter(fk_tipo__nombre="Hora inicio").all() | subtarea.objects.filter(
                                            fk_tarea__fk_plantilla__titulo = "PLANTILLA DE PRUEBA").filter(fk_tipo__nombre="Hora inicio y fin").all()
            plantilla_serializer = PlantillaTareaSubtareaSerializer(result, many = True)
            
            return Response(plantilla_serializer.data, status=status.HTTP_200_OK)

        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
     
