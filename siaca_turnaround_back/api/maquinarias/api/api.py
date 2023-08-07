from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import MaquinariaSerializer, MaquinariaModificarSerializer, MaquinariaTuraroundSerializer, MaquinariaDatosSerializer, MaquinariaTuraroundDatosSerializer, MaquinariaEstadoSerializer
from api.models import maquinaria, maquinaria_turnaround
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token


class Maquiarias(APIView):

    #Lista de Maquinarias
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinarias = maquinaria.objects.all()
                maquinaria_serializer = MaquinariaSerializer(maquinarias, many = True)
                return Response (maquinaria_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    #Crear una Maquinaria      
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinaria_serializer = MaquinariaDatosSerializer(data = request.data)
                if maquinaria_serializer.is_valid():
                    maquinaria_serializer.save()
                    return Response(maquinaria_serializer.data, status=status.HTTP_201_CREATED)
                return Response({'mensaje':'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class BuscarCategoria(APIView):
        
        #Buscar maquinarias por categoria
        def get(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinarias = maquinaria.objects.filter(fk_categoria = pk)
                if maquinarias:
                    maquinaria_serializer = MaquinariaSerializer(maquinarias, many = True)
                    return Response(maquinaria_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay maquinarias en esta categoria'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)


class ModificarMaquinaria(APIView):

        #Modificar maquinaria
        def put(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                machine = maquinaria.objects.filter(id = pk).first()
                if machine:
                    maquinaria_serializer = MaquinariaModificarSerializer(machine, data=request.data)
                    if maquinaria_serializer.is_valid():
                        maquinaria_serializer.save()
                        return Response(maquinaria_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No se ha encontrado la maquinaria'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
    #Eliminar una maquinaria
        def delete(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                machine = maquinaria.objects.filter(id = pk).first()
                if machine:
                    machine.delete()
                    return Response({'mensaje':'Maquinaria eliminada'}, status=status.HTTP_200_OK)
                return Response({'mensaje':'No se ha encontrado la maquinaria'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
class MaquinariaTurnaround(APIView):

    #Lista de Maquinarias
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinarias = maquinaria_turnaround.objects.all()
                maquinaria_serializer = MaquinariaTuraroundDatosSerializer(maquinarias, many = True)
                return Response (maquinaria_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    #Crear una Maquinaria      
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinaria_serializer = MaquinariaTuraroundDatosSerializer(data = request.data)
                if maquinaria_serializer.is_valid():
                    maquinaria_serializer.save()
                    return Response(maquinaria_serializer.data, status=status.HTTP_201_CREATED)
                return Response({'mensaje':'Datos no válidos'}, status=status.HTTP_201_CREATED)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
class EstadoMaquinaria(APIView):
     
     #Modificar estado de maquinaria
        def patch(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                machine = maquinaria.objects.filter(id = pk).first()
                if machine.estado == True:
                    maquinaria_serializer = MaquinariaEstadoSerializer(machine, data={"estado": False})
                    if maquinaria_serializer.is_valid():
                        maquinaria_serializer.save()
                        return Response(maquinaria_serializer.data, status=status.HTTP_200_OK)
                    
                else:
                        maquinaria_serializer = MaquinariaEstadoSerializer(machine, data={"estado": True})
                        if maquinaria_serializer.is_valid():
                            maquinaria_serializer.save()
                        return Response(maquinaria_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No se ha encontrado la maquinaria'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
     

        

