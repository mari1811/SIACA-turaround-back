from django.urls import path
from .api import MetricaUsoMaquinaria, MetricaTurnaroundPersonal, MetricaTurnaroundAerolineas, MetricaTurnaroundSLA, NumeroDeServicios, EstadisticaServicios, GraficaAerolineas,PorcentajeDepartamentos, TiemposPorVueloHoraInicioFin
from .api import NumeroDeVuelos, PorcentajeTurnaround, HoraInicio, HoraInicioYFin, PorcentajePlantillas, PorcentajeHora, PorcentajeHoraInicioFin, EstadisticaAerolinea, PorcentajeMaquinaria,TiemposPorVueloHoraInicio, VuelosOnTime
from .api import EstadisticaMaquinaria
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    #GET: Numero de usos de las maquinarias http://127.0.0.1:8000/metricas/maquinarias/?token=
    path('maquinarias/<str:fechaI>/<str:fechaF>/', MetricaUsoMaquinaria.as_view(), name='metrica_maquinarias'),

    #GET: Numero de turnarounds que ha participado http://127.0.0.1:8000/metricas/personal/?token=
    path('personal/<str:fechaI>/<str:fechaF>/', MetricaTurnaroundPersonal.as_view(), name='metrica_personal'),

    #GET: Numero de servicios que se ha realizado a cada aerolinea http://127.0.0.1:8000/metricas/aerolineas/?token=
    path('aerolineas/', MetricaTurnaroundAerolineas.as_view(), name='metrica_aerolineas'),

    #GET: Tiempo que duró el turnaround por vuelo ttp://127.0.0.1:8000/metricas/SLA/?token=
    path('SLA/', MetricaTurnaroundSLA.as_view(), name='metrica_SLA'),

    #GET: Numero de servicios que se ha realizado a cada aerolinea con  porcentaje general http://127.0.0.1:8000/metricas/turnaround-aerolineas/?token=
    path('turnaround-aerolineas/', PorcentajeTurnaround.as_view(), name='metrica_aerolinea_turnaround'),

    #GET: Informacion de las tareas de hora inicio realizadas con su turaround asociado http://127.0.0.1:8000/metricas/hora/?token=
    path('hora/', HoraInicio.as_view(), name='obtener_hora'),

    #GET: Informacion de las tareas de hora inicio y fin realizadas con su turaround asociado http://127.0.0.1:8000/metricas/horainiciofin/?token=
    path('horainiciofin/', HoraInicioYFin.as_view(), name='obtener_horainiciofin'),

    #GET: Numero de veces que se ha usado la plantilla y el porcentaje general de uso http://127.0.0.1:8000/metricas/plantillas/?token=
    path('plantillas/', PorcentajePlantillas.as_view(), name='metrica_plantilla'),

    #GET: Tiempo promedio de ejecución promedio de las subtareas de hora inicio http://127.0.0.1:8000/metricas/promedio-hora/?token=
    path('promedio-hora/', PorcentajeHora.as_view(), name='metrica_hora_promedio'),

    #GET: Tiempo promedio de ejecución promedio de las subtareas de hora inicio y fin  http://127.0.0.1:8000/metricas/promedio-horainiciofin/?token=
    path('promedio-horainiciofin/', PorcentajeHoraInicioFin.as_view(), name='metrica_horainiciofin_promedio'),

    #GET: Contador de vuelos culmiinados http://127.0.0.1:8000/metricas/contador-vuelos/?token=
    path('contador-vuelos/', NumeroDeVuelos.as_view(), name='contador_vuelos'),

    #GET: Contador de servicios realizados por cada tipo http://127.0.0.1:8000/metricas/contador-servicios/?token=
    path('contador-servicios/', NumeroDeServicios.as_view(), name='contador_servicios'),

    #GET: Estadistica de cual aeroliea lleva más servicios por cada servicio http://127.0.0.1:8000/metricas/estadistica-aerolinea/?token=
    path('estadistica-aerolinea/', EstadisticaAerolinea.as_view(), name='estadisitica_aerolinea'),

    #GET: Estadistica de cual aeroliea lleva más servicios por cada servicio http://127.0.0.1:8000/metricas/estadistica-servicios/?token=
    path('estadistica-servicios/', EstadisticaServicios.as_view(), name='estadisitica_servicios'),

    #GET: Numero de servicios por cada aerolinea por cada tipo de servicio http://127.0.0.1:8000/metricas/grafica-aerolinea/?token=
    path('grafica-aerolinea/', GraficaAerolineas.as_view(), name='grafica_aerolinea'),

    #GET: Porentaje de uso por categoria de maquinarias http://127.0.0.1:8000/metricas/porcentaje-maquinaria/?token=
    path('porcentaje-maquinaria/', PorcentajeMaquinaria.as_view(), name='porcentaje_maquinaria'),

    #GET: Porcentaje de participación por departamentos en los turnarounds http://127.0.0.1:8000/metricas/porcentaje-personal/?token=
    path('porcentaje-personal/', PorcentajeDepartamentos.as_view(), name='porcentaje_departementos'),

    #GET: Estadisticas de uso de maquinaria de las aerolineas http://127.0.0.1:8000/metricas/estadistica-maquinaria/?token=
    path('estadistica-maquinaria/', EstadisticaMaquinaria.as_view(), name='estadistica_maquinaria'),

    path('tiempo-vuelos-hora-inicio/<str:pk>/<str:fecha>/', TiemposPorVueloHoraInicio.as_view(), name='tiempo_inicio'),

    path('tiempo-vuelos-hora-inicio-fin/<str:pk>/<str:fecha>/', TiemposPorVueloHoraInicioFin.as_view(), name='tiempo_inicio_fin'),

    path('vuelos-on-time/', VuelosOnTime.as_view(), name='vuelos_on_time'),
]