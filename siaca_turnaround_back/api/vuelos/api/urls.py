from django.urls import path
from .api import  Vuelo, ModificarVuelo, BuscarVueloFecha, VueloDetalle, Ciudades, TipoVuelo, TipoServicio, ModificarCiudades, REG, BuscarVueloAerolinea
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[

    path('', Vuelo.as_view(), name='crear_vuelo'),
    path('lista/', Vuelo.as_view(), name='lista_vuelos'),
    path('<int:pk>/', ModificarVuelo.as_view(), name='modificar_vuelo'),
    path('buscar/<str:fecha>/', BuscarVueloFecha.as_view(), name= 'buscar_vuelo'),
    path('lista/detalles/', VueloDetalle.as_view(), name= 'buscar_vuelo'),
    path('lista/ciudades/', Ciudades.as_view(), name= 'ciudades'),
    path('lista/tipo-vuelo/', TipoVuelo.as_view(), name= 'tipo_vuelo'),
    path('lista/tipo-servicio/', TipoServicio.as_view(), name= 'tipo_servicio'),
    path('ciudades/', ModificarCiudades.as_view(), name= 'ciudades_agregar'),
    path('ciudades/<int:pk>/', ModificarCiudades.as_view(), name= 'ciudades_crud'),
    path('ac-reg/', REG.as_view(), name= 'ac_reg'),
    path('buscar-aerolinea/<int:pk>/', BuscarVueloAerolinea.as_view(), name= 'buscar_aerolinea'),
]