from django.urls import path
from .api import  Vuelo, ModificarVuelo, BuscarVueloFecha, VueloDetalle, Ciudades, TipoVuelo, TipoServicio, ModificarCiudades, REG, BuscarVueloAerolinea
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[

    #GET: Lista de vuelos, POST: Agregar un vuelo http://127.0.0.1:8000/vuelos/?token=
    path('', Vuelo.as_view(), name='crear_vuelo'),

    #GET: Lista de vuelos  http://127.0.0.1:8000/vuelos/lista/?token=
    path('lista/', Vuelo.as_view(), name='lista_vuelos'),

    #GET: Vuelo especifico por ID, PATCH: Editar vuelo, DELETE: eliminar vuelo http://127.0.0.1:8000/vuelos/<ID>/?token=
    path('<int:pk>/', ModificarVuelo.as_view(), name='modificar_vuelo'),

    #GET: Buscar vuelos por fecha http://127.0.0.1:8000/vuelos/buscar/AAAA-MM-DD/?token=
    path('buscar/<str:fecha>/', BuscarVueloFecha.as_view(), name= 'buscar_vuelo'),

    #GET: Lista de vuelos con todos los datos http://127.0.0.1:8000/vuelos/lista/detalles/?token=
    path('lista/detalles/', VueloDetalle.as_view(), name= 'buscar_vuelo'),

    #GET: Lista de ciudades http://127.0.0.1:8000/vuelos/lista/ciudades/?token=
    path('lista/ciudades/', Ciudades.as_view(), name= 'ciudades'),

    #GET: Lista de tipos de vuelo http://127.0.0.1:8000/vuelos/lista/tipo-vuelo/?token=
    path('lista/tipo-vuelo/', TipoVuelo.as_view(), name= 'tipo_vuelo'),

    #GET: Lista de tipos de servicios http://127.0.0.1:8000/vuelos/lista/tipo-servicio/?token=
    path('lista/tipo-servicio/', TipoServicio.as_view(), name= 'tipo_servicio'),

    #POST: Agregar ciudad  http://127.0.0.1:8000/vuelos/ciudades/?token=
    path('ciudades/', ModificarCiudades.as_view(), name= 'ciudades_agregar'),

    #GET: Buscar una ciudad especifica por ID PATCH: Editar ciudad, DELETE: Eliminar ciudad http://127.0.0.1:8000/vuelos/<ID>/ciudades/?token=
    path('ciudades/<int:pk>/', ModificarCiudades.as_view(), name= 'ciudades_crud'),

    #GET: Lista de REG http://127.0.0.1:8000/vuelos/ac-reg/?token=
    path('ac-reg/', REG.as_view(), name= 'ac_reg'),

    #GET: Lista de vuelos asociados a una aerolinea http://127.0.0.1:8000/vuelos/buscar-aerolinea/<ID>/?token=
    path('buscar-aerolinea/<int:pk>/', BuscarVueloAerolinea.as_view(), name= 'buscar_aerolinea'),
]