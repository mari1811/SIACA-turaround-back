from django.urls import path
from .api import MetricaUsoMaquinaria, MetricaTurnaroundPersonal, MetricaTurnaroundAerolineas, MetricaTurnaroundSLA, NumeroDeServicios, EstadisticaServicios, GraficaAerolineas
from .api import NumeroDeVuelos, PorcentajeTurnaround, HoraInicio, HoraInicioYFin, PorcentajePlantillas, PorcentajeHora, PorcentajeHoraInicioFin, EstadisticaAerolinea, PorcentajeMaquinaria
from .api import EstadisticaMaquinaria
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    path('maquinarias/', MetricaUsoMaquinaria.as_view(), name='metrica_maquinarias'),
    path('personal/', MetricaTurnaroundPersonal.as_view(), name='metrica_personal'),
    path('aerolineas/', MetricaTurnaroundAerolineas.as_view(), name='metrica_aerolineas'),
    path('SLA/', MetricaTurnaroundSLA.as_view(), name='metrica_SLA'),
    path('turnaround-aerolineas/', PorcentajeTurnaround.as_view(), name='metrica_aerolinea_turnaround'),
    path('hora/', HoraInicio.as_view(), name='obtener_hora'),
    path('horainiciofin/', HoraInicioYFin.as_view(), name='obtener_horainiciofin'),
    path('plantillas/', PorcentajePlantillas.as_view(), name='metrica_plantilla'),
    path('promedio-hora/', PorcentajeHora.as_view(), name='metrica_hora_promedio'),
    path('promedio-horainiciofin/', PorcentajeHoraInicioFin.as_view(), name='metrica_horainiciofin_promedio'),
    path('contador-vuelos/', NumeroDeVuelos.as_view(), name='contador_vuelos'),
    path('contador-servicios/', NumeroDeServicios.as_view(), name='contador_servicios'),
    path('estadistica-aerolinea/', EstadisticaAerolinea.as_view(), name='estadisitica_aerolinea'),
    path('estadistica-servicios/', EstadisticaServicios.as_view(), name='estadisitica_servicios'),
    path('grafica-aerolinea/', GraficaAerolineas.as_view(), name='grafica_aerolinea'),
    path('porcentaje-maquinaria/', PorcentajeMaquinaria.as_view(), name='porcentaje_maquinaria'),
    path('estadistica-maquinaria/', EstadisticaMaquinaria.as_view(), name='estadistica_maquinaria'),
]