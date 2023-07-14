from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import AerolineaSerializer
from api.models import aerolinea
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token


class Aerolinea(APIView):

    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                aerolineas = aerolinea.objects.all()
                aerolineas_serializer = AerolineaSerializer(aerolineas, many = True)
                return Response (aerolineas_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
            
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                aerolineas_serializer = AerolineaSerializer(data = request.data)
                if aerolineas_serializer.is_valid():
                    aerolineas_serializer.save()
                    return Response(aerolineas_serializer.data, status=status.HTTP_201_CREATED)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
class ModificarAerolinea(APIView):
    
    def get(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            fly = aerolinea.objects.filter(id = pk).first()
            if fly:
                aerolinea_serializer = AerolineaSerializer(fly)
                return Response(aerolinea_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado la aerolinea'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            fly = aerolinea.objects.filter(id = pk).first()
            if fly:
                aerolinea_serializer= AerolineaSerializer(fly, data=request.data)
                if aerolinea_serializer.is_valid():
                    aerolinea_serializer.save()
                    return Response(aerolinea_serializer.data, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado la aerolinea'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            fly = aerolinea.objects.filter(id = pk).first()
            if fly:
                fly.delete()
                return Response({'mensaje':'Aerolinea eliminada'}, status=status.HTTP_200_OK)
            return Response({'mensaje':'No se ha encontrado la aerolinea'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    