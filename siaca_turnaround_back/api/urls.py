from django.urls import path
from .views import MaquinariaView, CodigoDemoraView, TurnaroundView, UsuarioView, AerolineaView, PlantillaView, VueloView

urlpatterns=[
    path('maquinaria/',MaquinariaView.as_view(), name='maquinarias'),
    path('maquinaria/<int:id>',MaquinariaView.as_view(), name='maquina'),

    path('codigodemora/',CodigoDemoraView.as_view(), name='codigodemora'),

    path('turnaround/',TurnaroundView.as_view(), name='turnarounds'),

    path('usuario/',UsuarioView.as_view(), name='usuarios'),

    path('aerolinea/',AerolineaView.as_view(), name='aerolineas'),

    path('plantilla/',PlantillaView.as_view(), name='plantillas'),

    path('vuelo/',VueloView.as_view(), name='vuelos')
]