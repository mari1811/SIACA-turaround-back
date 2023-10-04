from django.urls import path
from .api import  Maquiarias, BuscarCategoria, ModificarMaquinaria, EstadoMaquinaria, ListaCategoria, BuscarMaquinaria, MaquinariaHistorial
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[

    path('', Maquiarias.as_view(), name='crear_maquinaria'),
    path('<int:pk>/', BuscarCategoria.as_view(), name='buscar_maquinaria'),
    path('modificar/<int:pk>/', ModificarMaquinaria.as_view(), name='buscar_maquinaria'),
    path('estado/<int:pk>/', EstadoMaquinaria.as_view(), name='estado_maquinaria'),
    path('categorias/', ListaCategoria.as_view(), name='lista_categoria'),
    path('buscar/<int:pk>/', BuscarMaquinaria.as_view(), name='maquinaria_buscar'),
    path('reserva/', MaquinariaHistorial.as_view(), name='maquinaria_reserva'),
    path('reserva/<str:fecha>/<str:horaI>/<str:horaF>/', MaquinariaHistorial.as_view(), name='maquinaria_reserva_categoria'),
]