from django.urls import path
from .api import Plantilla, Tarea, Subtarea, VistaPlantilla, VistaSubtarea, Maquinaria, VistaMaquinaria, Categoria
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    path('', Plantilla.as_view(), name='lista_plantillas'),
    path('tarea/', Tarea.as_view(), name='lista_tareas'),
    path('subtarea/', Subtarea.as_view(), name='lista_subtareas'),
    path('maquinaria/', Maquinaria.as_view(), name='lista_maquinaria'),
    path('maquinaria/<int:pk>/', VistaMaquinaria.as_view(), name='plantila_maquinaria'),
    path('categoria/', Categoria.as_view(), name='lista_categorias'),
    path('vista/<int:pk>/', VistaPlantilla.as_view(), name='vista'),
    path('subtarea/<int:pk>/', VistaSubtarea.as_view(), name='subtarea')

]

