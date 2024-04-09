from django.urls import path
from .api import  BuscarTurnaroundFecha, EliminarTurnaround, Codigos, Turnaround, TurnaroundDetalles, EditarTurnaround
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    #GET: Lista de turarounds, POST: Crear turnaround http://127.0.0.1:8000/turnarounds/?token=
    path('', Turnaround.as_view(), name='crear_turnaround'),

    #GET: Lista de códigos de demora de los vuelos http://127.0.0.1:8000/turnarounds/codigos/?token=
    path('codigos/', Codigos.as_view(), name='codigos_demora'),

    #GET: Lista de turnarounds por fecha http://127.0.0.1:8000/turnarounds/AAAA-MM-DD/?token=
    path('<str:fecha>/', BuscarTurnaroundFecha.as_view(), name='buscar_fecha'),

    #DELETE: Eliminar turnaround http://127.0.0.1:8000/turnarounds/eliminar/<ID>/?token=
    path('eliminar/<int:pk>/', EliminarTurnaround.as_view(), name='eliminar_turnaround'),

    #GET: Detalles de un turnaround por ID http://127.0.0.1:8000/turnarounds/detalles/<ID>/?token=
    path('detalles/<int:pk>/', TurnaroundDetalles.as_view(), name='detalles_turnaround'),

    #PATCH: Editar turnaround por ID http://127.0.0.1:8000/turnarounds/editar/<ID>/?token=
    path('editar/<int:pk>/', EditarTurnaround.as_view(), name='editar_turnaround'),
]