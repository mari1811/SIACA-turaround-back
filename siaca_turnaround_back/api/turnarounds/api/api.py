from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import TurnaroundSerializer, CodigosSerializer,  UsuarioTuraroundSerializer, TurnaroundDetallesSerializer,  TurnaroundFechaSerializer
from api.models import turnaround, usuario_turnaround, codigos_demora, maquinaria
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token


class Codigos(APIView):

    #Lista de Turnarounds
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                code = codigos_demora.objects.all()
                codigos_serializer = CodigosSerializer(code, many = True)
                return Response (codigos_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class Turnaround(APIView):


    #Lista de Turnarounds
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds = turnaround.objects.all()
                turnaround_serializer = TurnaroundDetallesSerializer(turnarounds, many = True)
                return Response (turnaround_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)

    #Crear un Turnaround      
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds_serializer = TurnaroundSerializer(data = request.data)
                if turnarounds_serializer.is_valid():
                    turnarounds_serializer.save()
                    return Response(turnarounds_serializer.data, status=status.HTTP_201_CREATED)
                else:
                     return Response({'mensaje':'Data no válida'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)

class BuscarTurnaroundFecha(APIView):
        
        def get(self, request, fecha=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds = turnaround.objects.filter(fecha_inicio = fecha)
                if turnarounds:
                    turnaround_serializer = TurnaroundFechaSerializer(turnarounds, many = True)
                    return Response(turnaround_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay vuelos en esa fecha'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
class EliminarTurnaround(APIView):
     
     def delete(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            turnarounds = turnaround.objects.filter(id = pk)
            if turnarounds:
                turnarounds.delete()
                return Response({'mensaje':'turnaround eliminado'}, status=status.HTTP_200_OK)
            return Response({'mensaje':'No existe este turnaround'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
     

class TurnaroundDetalles(APIView):
        
        def get(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds = turnaround.objects.filter(id = pk).first()
                if turnarounds:
                    turnaround_serializer = TurnaroundDetallesSerializer(turnarounds)
                    return Response(turnaround_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay vuelos en esa fecha'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        