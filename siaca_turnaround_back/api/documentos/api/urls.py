from django.urls import path
from .api import Documento, ComentarioTurnaround, HoraInicioFinTurnaround, HoraInicioTurnaround, ImagenTurnaround, TareasTurnaround
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    path('', Documento.as_view(), name='documentos'),
    path('comentario/', ComentarioTurnaround.as_view(), name='comentario_turnaround'),
    path('horainicio/', HoraInicioTurnaround.as_view(), name='horainicio_turnaround'),
    path('horainiciofin/', HoraInicioFinTurnaround.as_view(), name='horainiciofin_turnaround'),
    path('imagen/', ImagenTurnaround.as_view(), name='imagen_turnaround'),
    path('tareas/<int:pk>/', TareasTurnaround.as_view(), name='tareas_lista'),
]