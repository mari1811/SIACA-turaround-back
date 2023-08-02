from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import DocumentosDatosSerializer, VueloSerializer, DocumentosSerializer
from api.models import documento, vuelo
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token


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

