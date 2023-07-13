from django.urls import path
from .api import  Turnaround, BuscarTurnaroundFecha
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[

    path('', Turnaround.as_view(), name='crear_turnaround'),
    path('<str:fecha>/', BuscarTurnaroundFecha.as_view(), name='buscar_fecha'),
]