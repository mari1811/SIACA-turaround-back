from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import TurnaroundSerializer
from api.models import turnaround, usuario_turnaround, maquinaria_turnaround
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token


class Turnaround(APIView):

    #Lista de Turnarounds
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds = turnaround.objects.all()
                turnarounds_serializer = TurnaroundSerializer(turnarounds, many = True)
                return Response (turnarounds_serializer.data, status=status.HTTP_200_OK)

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
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class BuscarTurnaroundFecha(APIView):
        
        def get(self, request, fecha=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds = turnaround.objects.filter(fecha_inicio = fecha)
                if turnarounds:
                    turnaround_serializer = TurnaroundSerializer(turnarounds, many = True)
                    return Response(turnaround_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay vuelos en esa fecha'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        