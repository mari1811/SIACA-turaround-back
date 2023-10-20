from django.urls import path
from .api import  BuscarTurnaroundFecha, EliminarTurnaround, Codigos, Turnaround, TurnaroundDetalles
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    path('', Turnaround.as_view(), name='crear_turnaround'),
    path('codigos/', Codigos.as_view(), name='codigos_demora'),
    path('<str:fecha>/', BuscarTurnaroundFecha.as_view(), name='buscar_fecha'),
    path('eliminar/<int:pk>/', EliminarTurnaround.as_view(), name='eliminar_turnaround'),
    path('detalles/<int:pk>/', TurnaroundDetalles.as_view(), name='detalles_turnaround'),
    

]