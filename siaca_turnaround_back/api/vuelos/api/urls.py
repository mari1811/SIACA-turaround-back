from django.urls import path
from .api import  Vuelo, ModificarVuelo, BuscarVueloFecha, VueloDetalle
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[

    path('', Vuelo.as_view(), name='crear_vuelo'),
    path('lista/', Vuelo.as_view(), name='lista_vuelos'),
    path('<int:pk>/', ModificarVuelo.as_view(), name='modificar_vuelo'),
    path('buscar/<str:fecha>/', BuscarVueloFecha.as_view(), name= 'buscar_vuelo'),
    path('lista/detalles/', VueloDetalle.as_view(), name= 'buscar_vuelo')
]