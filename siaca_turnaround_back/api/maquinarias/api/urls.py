from django.urls import path
from .api import  Maquiarias, BuscarCategoria, ModificarMaquinaria, EstadoMaquinaria, ListaCategoria, BuscarMaquinaria, MaquinariaHistorial
from .api import MetricaUsoMaquinaria, MaquinariaTurnaround
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[
    #GET: Lista de maquinaria, POST: Crear maquinaria http://127.0.0.1:8000/maquinarias/?token=
    path('', Maquiarias.as_view(), name='crear_maquinaria'),

    #GET: Buscar maquinarias asociadas a la categoria por ID http://127.0.0.1:8000/maquinarias/<ID>/?token=
    path('<int:pk>/', BuscarCategoria.as_view(), name='buscar_maquinaria'),

    #PATCH: Modificar maquinaria por ID, DELETE: Eliminar una maquinaria por ID http://127.0.0.1:8000/maquinarias/modificar/<ID>/?token=
    path('modificar/<int:pk>/', ModificarMaquinaria.as_view(), name='buscar_maquinaria'),

    #PATCH: Cambiar el estado de la maquinaria por ID http://127.0.0.1:8000/maquinarias/estado/<ID>/?token=
    path('estado/<int:pk>/', EstadoMaquinaria.as_view(), name='estado_maquinaria'),

    #GET: Lista de categorias de maquinarias http://127.0.0.1:8000/maquinarias/categorias/?token=
    path('categorias/', ListaCategoria.as_view(), name='lista_categoria'),

    #GET: Buscar maquinaria por ID http://127.0.0.1:8000/maquinarias/buscar/<ID>/?token=
    path('buscar/<int:pk>/', BuscarMaquinaria.as_view(), name='maquinaria_buscar'),

    #POST: Asignar maquinaria a un turnaround http://127.0.0.1:8000/maquinarias/reserva/?token=
    path('reserva/', MaquinariaHistorial.as_view(), name='maquinaria_reserva'),

    #GET: Lista de maquinarias disponiles en la fecha y rango de hora http://127.0.0.1:8000/maquinarias/reserva/<fecha>/<horaInicio>/<horaFin>/?token=
    path('reserva/<str:fecha>/<str:horaI>/<str:horaF>/', MaquinariaHistorial.as_view(), name='maquinaria_reserva_categoria'),

    #GET: Metrica de numero de usos de maquinarias http://127.0.0.1:8000/maquinarias/metrica/uso/?token=
    path('metrica/uso/', MetricaUsoMaquinaria.as_view(), name='metrica_uso'),

    #GET: Lista de maquinarias asociadas a un turnaround por ID de turaround http://127.0.0.1:8000/maquinarias/lista/<ID>/?token=
    path('lista/<int:pk>/', MaquinariaTurnaround.as_view(), name='maquinarias_turnaround'),
]
