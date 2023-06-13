from django.urls import path
from .views import MaquinariaView, CodigoDemoraView, TurnaroundView, UsuarioView, AerolineaView, PlantillaView, VueloView, TareaView, SubtareaView


urlpatterns=[
    path('maquinaria/',MaquinariaView.as_view(), name='maquinarias'),
    path('maquinaria/<int:id>',MaquinariaView.as_view(), name='maquina'),

    path('codigodemora/',CodigoDemoraView.as_view(), name='codigodemora'),

    path('turnaround/',TurnaroundView.as_view(), name='turnarounds'),

    path('usuario/',UsuarioView.as_view(), name='usuarios'),
    path('usuario/<int:id>',UsuarioView.as_view(), name='usuario'),

    path('aerolinea/',AerolineaView.as_view(), name='aerolineas'),
    path('aerolinea/<int:id>',AerolineaView.as_view(), name='aerolinea'),

    path('plantilla/',PlantillaView.as_view(), name='plantillas'),
    path('plantilla/<int:id>',PlantillaView.as_view(), name='plantilla'),

    path('tarea/',TareaView.as_view(), name='tareas'),
    path('tarea/<int:id>',TareaView.as_view(), name='tarea'),

    path('subtarea/',SubtareaView.as_view(), name='subtarea'),
    path('subtarea/<int:id>',SubtareaView.as_view(), name='subtarea'),

    path('vuelo/',VueloView.as_view(), name='vuelos'),
    path('vuelo/<int:id>',VueloView.as_view(), name='vuelo')
]