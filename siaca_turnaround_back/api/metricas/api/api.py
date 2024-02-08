from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from api.models import maquinaria, categoria, maquinaria_historial, usuario_turnaround, turnaround, aerolinea, vuelo, plantilla, Hora, HoraInicioFin, subtarea
from .serializer import PlantillaSerializer, VueloSerializer, HoraInicioSerializer, HoraInicioFinSerializer
from rest_framework import filters
from rest_framework import generics
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta
from django.db.models import Count, Sum, F, Value, Func, CharField, DateTimeField, TimeField, Subquery, Min, Max
from django.db.models import  FloatField, ExpressionWrapper, F, Avg, Q, DurationField, IntegerField, fields
from django.db.models.functions import Concat, Cast
from django.db.models.functions.datetime import TruncHour
from django.db.models import Func

from django.db.models import Case, When

from django.db.models import Avg

from django.db import connection



class MetricaUsoMaquinaria(APIView):
        
        #Metrica de numero de usos de maquinarias 
        def get(self, request, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                maquinarias = maquinaria_historial.objects.values('fk_maquinaria__fk_categoria__nombre','fk_maquinaria__identificador','fk_maquinaria_id','fecha').annotate(contador=Count('fk_maquinaria__identificador')).filter(contador__gt=0)
                if maquinarias:
                    return Response(maquinarias , status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay maquinarias'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        
class MetricaTurnaroundPersonal(APIView):
        
        #Metrica de numero de turnarounds que ha participado el personal
        def get(self, request, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                usuarios = usuario_turnaround.objects.values( 'fk_usuario__id','fk_usuario__fk_departamento__nombre','fk_usuario__fk_cargo__nombre')
                contador = usuarios.annotate(contador=Count('fk_usuario__id')).filter(contador__gt=0).annotate(full_name=Concat('fk_usuario__fk_user__first_name', Value(' '), 'fk_usuario__fk_user__last_name',  output_field=CharField()))
                if usuarios:
                    return Response(contador , status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay turnarounds'}, status=status.HTTP_400_BAD_REQUEST)
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
                return Response({'mensaje':'No hay aerolineas'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)

#Clase que define variables tipo hora    
class TimeDiff(Func):
    function = 'TIMEDIFF'
    output_field = TimeField()        
        
class MetricaTurnaroundSLA(APIView):
        
        #Metrica de tiempo que han tardado los turnarounds
        def get(self, request, *args, **kwargs):
            token = request.GET.get('token')
            token = Token.objects.filter(key = token).first()
            if token:
                turnarounds = turnaround.objects.annotate(tiempo=TimeDiff(F('hora_fin'), F('hora_inicio'))).filter(tiempo__isnull=False).values('tiempo', 'id', 'fk_vuelo__numero_vuelo')
                if turnarounds:
                    return Response( turnarounds, status=status.HTTP_200_OK)
                return Response({'mensaje':'No hay turnarounds'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
        


class PorcentajeTurnaround(APIView):

    #Porcentaje turnarounds por aerolinea
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            if request.method == 'GET':
                plantillas = turnaround.objects.values('fk_vuelo__fk_aerolinea__nombre','fk_vuelo__fk_aerolinea__id').annotate(
                            contador=Count('fk_vuelo__fk_aerolinea__nombre'),
                            porcentaje=ExpressionWrapper(
                            Count('fk_vuelo__fk_aerolinea__nombre') * 100 / turnaround.objects.count(),
                            output_field=CharField()),
                            percent=Concat('porcentaje', Value('%'), output_field=CharField()))
                            
                return Response( plantillas , status=status.HTTP_200_OK)
            return Response({'mensaje':'No hay turnarounds'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
#Clase que convierte minutos en horas
class DiffInMinutes(Func):
    function = 'TIMESTAMPDIFF'
    template = '%(function)s(MINUTE, %(expressions)s), TIMESTAMPDIFF(SECOND, %(expressions)s)'
    output_field = IntegerField()
    
class HoraInicio(APIView):
     
     #Hora inicio tareas y subtareas por plantilla
     def get (self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            result = Hora.objects.filter(fk_subtarea__fk_tarea__fk_plantilla__titulo = "Plantilla prueba").annotate(tiempo=DiffInMinutes('fk_turnaround__hora_inicio', 'hora_inicio')).values('id','fk_subtarea__id','fk_subtarea__titulo','fk_subtarea__fk_tarea__id','fk_subtarea__fk_tarea__titulo',
                                                  'fk_subtarea__fk_tarea__fk_plantilla__id','fk_subtarea__fk_tarea__fk_plantilla__titulo','fk_subtarea__fk_tipo__id','fk_subtarea__fk_tipo__nombre',
                                                  'fk_turnaround__id','fk_turnaround__fk_vuelo__fk_aerolinea__nombre','fk_turnaround__hora_inicio','fk_turnaround__hora_fin','hora_inicio','tiempo')
            
            return Response(result, status=status.HTTP_200_OK)

        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
     

class HoraInicioYFin(APIView):
    
    #Hora inicio y final tareas y subtareas por plantilla
     def get (self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            result = HoraInicioFin.objects.filter(fk_subtarea__fk_tarea__fk_plantilla__titulo = "Plantilla prueba").annotate(tiempo=DiffInMinutes('hora_inicio', 'hora_fin')).values('id','fk_subtarea__id','fk_subtarea__titulo','fk_subtarea__fk_tarea__id','fk_subtarea__fk_tarea__titulo',
                                                  'fk_subtarea__fk_tarea__fk_plantilla__id','fk_subtarea__fk_tarea__fk_plantilla__titulo','fk_subtarea__fk_tipo__id','fk_subtarea__fk_tipo__nombre',
                                                  'fk_turnaround__id','fk_turnaround__fk_vuelo__fk_aerolinea__nombre','fk_turnaround__hora_inicio','fk_turnaround__hora_fin','hora_inicio','hora_fin','tiempo')
            
            return Response(result, status=status.HTTP_200_OK)

        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)


class PorcentajePlantillas(APIView):

    #Porcentaje de usos de plantillas
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            if request.method == 'GET':
                plantillas = vuelo.objects.values('fk_plantilla__id','fk_plantilla__titulo').annotate(
                            contador=Count('fk_plantilla__id'),
                            porcentaje=ExpressionWrapper(
                            Count('fk_plantilla__id') * 100 / vuelo.objects.count(),
                            output_field=CharField()),
                            percent=Concat('porcentaje', Value('%'), output_field=CharField()))
                            
                return Response( plantillas , status=status.HTTP_200_OK)
            return Response({'mensaje':'No hay turnarounds'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
def tiempo_transcurrido_horas(duracion):
                segundos = duracion.total_seconds()
                horas, segundos = divmod(segundos, 3600)
                minutos, segundos = divmod(segundos, 60)
                return '{:02d}:{:02d}:{:02d}'.format(int(horas), int(minutos), int(segundos))
    

class PorcentajeHora(APIView):

    #Hora inicio tiempo promedio de subtareas 
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key=token).first()
        if token:

            def obtener_tiempo_transcurrido(datos):
                tiempo_transcurrido = datos.annotate(
                    tiempo_transcurrido=ExpressionWrapper(
                        F('hora_inicio') - F('fk_turnaround__hora_inicio'), output_field=DurationField()
                    )
                )
                return tiempo_transcurrido

            def obtener_promedio_tiempo_transcurrido(datos):
                promedio_tiempo_transcurrido = datos.values('fk_subtarea_id','fk_subtarea__titulo','fk_subtarea__fk_tarea__titulo',
                                                            'fk_subtarea__fk_tarea__fk_plantilla__titulo','fk_subtarea__fk_tarea__fk_plantilla__id',
                                                            'fk_subtarea__fk_tipo_id').annotate(
                    average_tiempo_transcurrido=Avg('tiempo_transcurrido')
                )
                return promedio_tiempo_transcurrido

            datos = Hora.objects.values('hora_inicio', 'fk_turnaround__hora_inicio',"fk_subtarea_id",'fk_subtarea__fk_tarea__fk_plantilla__id','fk_subtarea__fk_tipo_id')
            tiempo_transcurrido = obtener_tiempo_transcurrido(datos)
            promedio_tiempo_transcurrido = obtener_promedio_tiempo_transcurrido(tiempo_transcurrido)

            for dato in promedio_tiempo_transcurrido:
                dato['average_tiempo_transcurrido'] = tiempo_transcurrido_horas(dato['average_tiempo_transcurrido'])

            return Response(promedio_tiempo_transcurrido, status=status.HTTP_200_OK)

        return Response({'mensaje': 'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class PorcentajeHoraInicioFin(APIView):

    #Hora inicio tiempo promedio de subtareas 
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key=token).first()
        if token:

            def obtener_tiempo_transcurrido(datos):
                tiempo_transcurrido = datos.annotate(
                    tiempo_transcurrido=ExpressionWrapper(
                        F('hora_fin') - F('hora_inicio'), output_field=DurationField()
                    )
                )
                return tiempo_transcurrido

            def obtener_promedio_tiempo_transcurrido(datos):
                promedio_tiempo_transcurrido = datos.values('fk_subtarea_id','fk_subtarea__titulo','fk_subtarea__fk_tarea__titulo',
                                                            'fk_subtarea__fk_tarea__fk_plantilla__titulo','fk_subtarea__fk_tarea__fk_plantilla__id',
                                                            'fk_subtarea__fk_tipo_id').annotate(
                    average_tiempo_transcurrido=Avg('tiempo_transcurrido')
                )
                return promedio_tiempo_transcurrido

            datos = HoraInicioFin.objects.values('hora_inicio', 'hora_fin',"fk_subtarea_id","fk_turnaround__hora_inicio",'fk_subtarea__fk_tarea__fk_plantilla__id',
                                                 'fk_subtarea__fk_tipo_id')
            tiempo_transcurrido = obtener_tiempo_transcurrido(datos)
            promedio_tiempo_transcurrido = obtener_promedio_tiempo_transcurrido(tiempo_transcurrido)

            for dato in promedio_tiempo_transcurrido:
                dato['average_tiempo_transcurrido'] = tiempo_transcurrido_horas(dato['average_tiempo_transcurrido'])

            return Response(promedio_tiempo_transcurrido, status=status.HTTP_200_OK)

        return Response({'mensaje': 'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class NumeroDeVuelos(APIView):

    #Numero de vuelos realizados 
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            if request.method == 'GET':
                vuelos = vuelo.objects.filter(estado = "No ha llegado").count()
                            
                return Response( {"numero_servicios": vuelos} , status=status.HTTP_200_OK)
            return Response({'mensaje':'No hay turnarounds'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class NumeroDeServicios(APIView):

    #Numero de servicios realizados por cada tipo de servicio
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
            if request.method == 'GET':
                servicios = vuelo.objects.values('tipo_servicio__nombre').annotate(contador=Count('id')).filter(contador__gt=0)
                            
                return Response( servicios , status=status.HTTP_200_OK)
            return Response({'mensaje':'No hay turnarounds'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje':'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

def time_hours(duracion):
    if duracion is None:
        return '00:00:00'
    segundos = duracion.total_seconds()
    horas, segundos = divmod(segundos, 3600)
    minutos, segundos = divmod(segundos, 60)
    return '{:02d}:{:02d}:{:02d}'.format(int(horas), int(minutos), int(segundos))

class EstadisticaAerolinea(APIView):

    #Hora inicio tiempo promedio de subtareas 
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key=token).first()
        if token:

            def obtener_tiempo_transcurrido(datos):
                tiempo_transcurrido = datos.annotate(
                    tiempo_transcurrido=ExpressionWrapper(
                        F('hora_fin') - F('hora_inicio'), output_field=DurationField()
                    )
                )
                return tiempo_transcurrido

            def obtener_promedio_tiempo_transcurrido(datos):
                promedio_tiempo_transcurrido = datos.values('fk_vuelo__fk_aerolinea__nombre','fk_vuelo__tipo_servicio__nombre','fk_vuelo__tipo_servicio__id').annotate(
                    average_tiempo_transcurrido=Avg('tiempo_transcurrido'), contador=Count('id')
                ).filter(contador__gt=0)

                return promedio_tiempo_transcurrido

            datos = turnaround.objects.values('hora_inicio', 'hora_fin').filter(fk_vuelo__estado="Finalizado")
            tiempo_transcurrido = obtener_tiempo_transcurrido(datos)
            promedio_tiempo_transcurrido = obtener_promedio_tiempo_transcurrido(tiempo_transcurrido)

            for dato in promedio_tiempo_transcurrido:
                dato['average_tiempo_transcurrido'] = time_hours(dato['average_tiempo_transcurrido'])

            return Response(promedio_tiempo_transcurrido, status=status.HTTP_200_OK)

        return Response({'mensaje': 'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
class EstadisticaServicios(APIView):

    #Hora inicio tiempo promedio de subtareas 
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key=token).first()
        if token:

            datos = vuelo.objects.values('tipo_servicio__nombre').annotate(aerolinea=Max('fk_aerolinea__nombre')).order_by('tipo_servicio__nombre')

            return Response(datos, status=status.HTTP_200_OK)

        return Response({'mensaje': 'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
    
class GraficaAerolineas(APIView):

    #Hora inicio tiempo promedio de subtareas 
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key=token).first()
        if token:

            resultados = []

            # Obtener todas las aerolíneas
            aerolineas = vuelo.objects.values('fk_aerolinea','fk_aerolinea__nombre').distinct()

            # Iterar sobre cada aerolínea
            for datos in aerolineas:
                aerolinea_id = datos['fk_aerolinea']
                aerolinea_nombre = datos['fk_aerolinea__nombre']

                # Contadores para cada tipo de servicio
                turnaround_entrante = 0
                turnaround_saliente = 0
                inbound = 0
                outbound = 0

                # Obtener todos los vuelos de la aerolínea
                vuelos = vuelo.objects.filter(fk_aerolinea=aerolinea_id)

                # Iterar sobre cada vuelo
                for servicio in vuelos:
                    # Verificar el tipo de servicio y actualizar el contador correspondiente
                    if servicio.tipo_servicio.nombre == 'Turnaround entrante':
                        turnaround_entrante += 1
                    elif servicio.tipo_servicio.nombre == 'Turnaround saliente':
                        turnaround_saliente += 1
                    elif servicio.tipo_servicio.nombre == 'Inbound':
                        inbound += 1
                    elif servicio.tipo_servicio.nombre == 'Outbound':
                        outbound += 1

                # Agregar los resultados a la lista
                resultados.append({
                    'nombre_aerolinea': aerolinea_nombre,
                    'turnaround_entrante': turnaround_entrante,
                    'turnaround_saliente': turnaround_saliente,
                    'inbound': inbound,
                    'outbound': outbound
                })

            return Response(resultados, status=status.HTTP_200_OK)

        return Response({'mensaje': 'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    
class PorcentajeMaquinaria(APIView):
    
    #Porcentaje de uso de las maquinarias
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
                maquinarias = maquinaria_historial.objects.values('fk_maquinaria__fk_categoria__nombre').all()
                categorias = maquinaria_historial.objects.values('fk_maquinaria__fk_categoria__nombre').distinct()
                
                porcentajes = []
                for c in categorias:
                    cantidad_usos = maquinarias.filter(fk_maquinaria__fk_categoria__nombre=c['fk_maquinaria__fk_categoria__nombre']).count()
                    porcentaje = (cantidad_usos / maquinarias.count()) * 100
                    porcentajes.append({'categoria': c['fk_maquinaria__fk_categoria__nombre'], 'porcentaje': porcentaje})
                    
                return Response(porcentajes, status=status.HTTP_200_OK)

        return Response({'mensaje': 'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    

class PorcentajeDepartamentos(APIView):
    
    #Porcentaje de uso de las maquinarias
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key = token).first()
        if token:
                personal = usuario_turnaround.objects.values('fk_usuario__fk_departamento__nombre').all()
                departamentos = usuario_turnaround.objects.values('fk_usuario__fk_departamento__nombre').distinct()
                
                porcentajes = []
                for d in departamentos:
                    cantidad_usos = personal.filter(fk_usuario__fk_departamento__nombre=d['fk_usuario__fk_departamento__nombre']).count()
                    porcentaje = (cantidad_usos / personal.count()) * 100
                    porcentajes.append({'departamentos': d['fk_usuario__fk_departamento__nombre'], 'porcentaje': porcentaje})
                    
                return Response(porcentajes, status=status.HTTP_200_OK)

        return Response({'mensaje': 'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)

    
class EstadisticaMaquinaria(APIView):

    #Estadisticas de numero de usos de maquinarias
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        token = Token.objects.filter(key=token).first()
        if token:

            datos = maquinaria_historial.objects.values('fk_maquinaria__fk_categoria__nombre').annotate(aerolinea=Max('fk_turnaround__fk_vuelo__fk_aerolinea__nombre'), 
                                                                                                        maquinaria_max=Max('fk_maquinaria__identificador')).order_by('fk_maquinaria__fk_categoria__nombre')

            return Response(datos, status=status.HTTP_200_OK)

        return Response({'mensaje': 'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)
    