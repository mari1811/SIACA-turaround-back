from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import VueloSerializer, ListaVuelosSerializer
from api.models import vuelo
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token


class Vuelo(APIView):

    #Lista de Vuelos
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                vuelos = vuelo.objects.all()
                vuelos_serializer = VueloSerializer(vuelos, many = True)
                return Response (vuelos_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    #Crear un Vuelo      
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                vuelos_serializer = VueloSerializer(data = request.data)
                if vuelos_serializer.is_valid():
                    vuelos_serializer.save()
                    return Response(vuelos_serializer.data, status=status.HTTP_201_CREATED)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)

class ModificarVuelo(APIView):
    
    #Buscar un vuelo específico
    def get(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            fly = vuelo.objects.filter(id = pk).first()
            if fly:
                vuelo_serializer = ListaVuelosSerializer(fly)
                return Response(vuelo_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado el vuelo'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    #Editar un vuelo
    def put(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            fly = vuelo.objects.filter(id = pk).first()
            if fly:
                vuelo_serializer = VueloSerializer(fly, data=request.data)
                if vuelo_serializer.is_valid():
                    vuelo_serializer.save()
                    return Response(vuelo_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado el vuelo'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
    #Eliminar un vuelo
    def delete(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            fly = vuelo.objects.filter(id = pk).first()
            if fly:
                fly.delete()
                return Response({'mensaje':'Vuelo eliminado'}, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado el vuelo'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    
class VueloDetalle(APIView):

    #Lista de Vuelos
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                vuelos = vuelo.objects.all()
                vuelos_serializer = ListaVuelosSerializer(vuelos, many = True)
                return Response (vuelos_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    


class BuscarVueloFecha(APIView):
        
        def get(self, request, fecha=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                fly = vuelo.objects.filter(fecha_llegada = fecha)
                if fly:
                    vuelo_serializer = ListaVuelosSerializer(fly, many = True)
                    return Response(vuelo_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay vuelos en esa fecha'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        


    








