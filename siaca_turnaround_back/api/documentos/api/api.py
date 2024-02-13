from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import DocumentosDatosSerializer, VueloSerializer, DocumentosSerializer, HoraInicioSerializer, HoraInicioFinSerializer, ImagenSerializer, ComentarioSerializer, TurnaoundSerializer
from api.models import documento, vuelo, maquinaria, Hora, HoraInicioFin, Comentario, Imagen, turnaround
from api.models import turnaround, subtarea, Imagen, Hora, HoraInicioFin, Comentario
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token
import json
from django.http import JsonResponse
from django.core.serializers import serialize

class Documento(APIView):

    #Lista de Docuemntos
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                documentos = documento.objects.all()
                documento_serializer = DocumentosDatosSerializer(documentos, many = True)
                return Response (documento_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)

    #Crear un Documento      
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                documento_serializer = DocumentosSerializer(data = request.data)
                if documento_serializer.is_valid():
                    documento_serializer.save()
                    return Response(documento_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response({'mensaje':'Data no válida'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class ComentarioTurnaround(APIView):

        #Agregar comentario a una subtarea del turaround
        def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds_serializer = ComentarioSerializer(data = request.data)
                if turnarounds_serializer.is_valid():
                    turnarounds_serializer.save()
                    return Response(turnarounds_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response({'mensaje':'Data no válida'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)


class HoraInicioTurnaround(APIView):

        #Agregar hora de inicio a una subtarea del turnaround
        def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds_serializer = HoraInicioSerializer(data = request.data)
                if turnarounds_serializer.is_valid():
                    turnarounds_serializer.save()
                    return Response(turnarounds_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response({'mensaje':'Data no válida'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class HoraInicioFinTurnaround(APIView):

        #Agregar hora de inicio y fin a una subtarea del turnaround 
        def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds_serializer = HoraInicioFinSerializer(data = request.data)
                if turnarounds_serializer.is_valid():
                    turnarounds_serializer.save()
                    return Response(turnarounds_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response({'mensaje':'Data no válida'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
class ImagenTurnaround(APIView):

        #Agregar hora una imagen a una subtarea del turnaround      
        def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds_serializer = ImagenSerializer(data = request.data)
                if turnarounds_serializer.is_valid():
                    turnarounds_serializer.save()
                    return Response(turnarounds_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response({'mensaje':'Data no válida'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class TareasTurnaround(APIView):

    #Turnaround por ID con la infomación del vuelo y la plantilla asociada
    def get(self, request, pk=None, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                datos = turnaround.objects.filter(id = pk).first()
                documento_serializer = TurnaoundSerializer(datos)
                return Response (documento_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class Turnarounds(APIView):

    #Turnaround por ID con la infomación del vuelo y la plantilla asociada
    def get(self, request, pk=None, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                imagenes = list(Imagen.objects.filter(fk_turnaround_id=pk).values('fk_subtarea__id','fk_subtarea__titulo', 'imagen','fk_subtarea__fk_tipo__nombre','fk_subtarea__fk_tarea__titulo'))
                horas = list(Hora.objects.filter(fk_turnaround_id=pk).values('fk_subtarea__id','fk_subtarea__titulo', 'hora_inicio','fk_subtarea__fk_tipo__nombre','fk_subtarea__fk_tarea__titulo'))
                horas_inicio_fin = list(HoraInicioFin.objects.filter(fk_turnaround_id=pk).values('fk_subtarea__id','fk_subtarea__titulo', 'hora_inicio', 'hora_fin','fk_subtarea__fk_tipo__nombre','fk_subtarea__fk_tarea__titulo'))
                comentarios = list(Comentario.objects.filter(fk_turnaround_id=pk).values('fk_subtarea__id','fk_subtarea__titulo', 'comentario','fk_subtarea__fk_tipo__nombre','fk_subtarea__fk_tarea__titulo'))


                return Response({
                'horas': horas,
                'horas_inicio_fin': horas_inicio_fin,
                'imagenes': imagenes,
                'comentarios': comentarios
            })

