from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from api.models import maquinaria, categoria, maquinaria_historial, usuario_turnaround, turnaround, aerolinea, vuelo
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta
from django.db.models import Count, Sum, F, Value, Func, CharField, DateTimeField, TimeField
from django.db.models.functions import Concat, Cast
from django.db.models.functions.datetime import TruncHour



class MetricaUsoMaquinaria(APIView):
        
        #Metrica de numero de usos de maquinarias 
        def get(self, request, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinarias = maquinaria_historial.objects.values('fk_maquinaria__fk_categoria__nombre','fk_maquinaria__identificador','fk_maquinaria_id').annotate(contador=Count('fk_maquinaria__identificador')).filter(contador__gt=0)
                if maquinarias:
                    return Response(maquinarias , status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay maquinarias en esta categoria'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
class MetricaTurnaroundPersonal(APIView):
        
        #Metrica de numero de turnarounds que han participado
        def get(self, request, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                usuarios = usuario_turnaround.objects.values( 'fk_usuario__id','fk_usuario__departamento')
                contador = usuarios.annotate(contador=Count('fk_usuario__id')).filter(contador__gt=0).annotate(full_name=Concat('fk_usuario__fk_user__first_name', Value(' '), 'fk_usuario__fk_user__last_name',  output_field=CharField()))
                if usuarios:
                    return Response(contador , status=status.HTTP_200_OK)
                return Response({'mensaje':'No se hay turnarounds'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
class MetricaTurnaroundAerolineas(APIView):
        
        #Metrica de turnarounds de una aerolinea
        def get(self, request, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                aerolineas = vuelo.objects.values('fk_aerolinea__nombre').annotate(contador=Count('fk_aerolinea__nombre')).filter(contador__gt=0)
                if aerolineas:
                    return Response( aerolineas, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay vuelos'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        

class MetricaTurnaroundSLA(APIView):
        
        #Metrica de tiempo que han tardado los turnarounds
        def get(self, request, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                aerolineas = turnaround.objects.extra(select={'tiempo': '(TIME_TO_SEC(TIMEDIFF(hora_fin, hora_inicio)) DIV 60)',}).values('tiempo', 'id', 'fk_vuelo__numero_vuelo')
                if aerolineas:
                    return Response( aerolineas, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay vuelos'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)