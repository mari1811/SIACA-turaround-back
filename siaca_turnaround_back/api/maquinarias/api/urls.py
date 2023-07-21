from django.urls import path
from .api import  Maquiarias, BuscarCategoria, ModificarMaquinaria, MaquinariaTurnaround
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[

    path('', Maquiarias.as_view(), name='crear_maquinaria'),
    path('<int:pk>/', BuscarCategoria.as_view(), name='buscar_maquinaria'),
    path('modificar/<int:pk>/', ModificarMaquinaria.as_view(), name='buscar_maquinaria'),
    path('turnaround/', MaquinariaTurnaround.as_view(), name='buscar_maquinaria')
]