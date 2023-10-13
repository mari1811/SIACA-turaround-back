from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import MaquinariaSerializer, MaquinariaModificarSerializer, MaquinariaDatosSerializer, MaquinariaEstadoSerializer, ListaCategoriaSerializer, ModificarSerializer, MaquinariaHistorialSerializer, MaquinariaCategoriaSerializer
from api.models import maquinaria, categoria, maquinaria_historial
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta
from django.db.models import Count, Sum


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
        
class ListaCategoria(APIView):

    #Lista de Maquinarias
    def get(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                categorias = categoria.objects.all()
                categorias_serializer = ListaCategoriaSerializer(categorias, many = True)
                return Response (categorias_serializer.data, status=status.HTTP_200_OK)

            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)


class ModificarMaquinaria(generics.RetrieveUpdateDestroyAPIView):

        #Modificar maquinaria
        def patch(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                machine = maquinaria.objects.filter(id = pk).first()
                if machine:
                    maquinaria_serializer = ModificarSerializer(machine, data=request.data)
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


class BuscarMaquinaria(APIView):
        
        #Buscar maquinarias por categoria
        def get(self, request, pk=None, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinarias = maquinaria.objects.filter(id = pk).first()
                if maquinarias:
                    maquinaria_serializer = MaquinariaModificarSerializer(maquinarias)
                    return Response(maquinaria_serializer.data, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay maquinarias en esta categoria'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class MaquinariaHistorial(APIView):
     
    #Asignar hora inicio y fin     
    def post(self, request, *args, **kwargs):
        
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinaria_serializer = MaquinariaHistorialSerializer(data = request.data)
                if maquinaria_serializer.is_valid():
                    maquinaria_serializer.save()
                    return Response(maquinaria_serializer.data, status=status.HTTP_201_CREATED)
                return Response({'mensaje':'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    #Buscar maquinarias por categoria
    def get(self, request, fecha=None, horaI=None, horaF=None, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            hourI= datetime.strptime(horaI, '%H:%M')
            hourF= datetime.strptime(horaF, '%H:%M')
            min = timedelta(minutes=30)
            max = timedelta(minutes=60)
            maquinarias = maquinaria_historial.objects.filter(fecha = fecha).filter(hora_inicio__range = (hourI - min, hourF + max)).all() | maquinaria_historial.objects.filter(fecha = fecha).filter(hora_fin__range = (hourI - min, hourF + max)).all()
            if maquinarias:
                maquinaria_serializer = MaquinariaCategoriaSerializer(maquinarias, many = True)
                return Response(maquinaria_serializer.data, status=status.HTTP_200_OK)
            return Response([{}])
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class MetricaUsoMaquinaria(APIView):
        
        #Metrica de numeor de usos de maquinarias 
        def get(self, request, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinarias = maquinaria_historial.objects.values('fk_maquinaria__fk_categoria__nombre','fk_maquinaria__identificador','fk_maquinaria_id').annotate(contador=Count('fk_maquinaria__identificador')).filter(contador__gt=0)
                if maquinarias:
                    return Response(maquinarias , status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay maquinarias en esta categoria'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
     
     
     

        

