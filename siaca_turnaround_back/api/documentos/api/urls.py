from django.urls import path
from .api import Documento, ComentarioTurnaround, HoraInicioFinTurnaround, HoraInicioTurnaround, ImagenTurnaround, TareasTurnaround, Turnarounds, HoraInicioYFin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    #GET: Lista de docuemntos, POST: Crear un nuevo documento http://127.0.0.1:8000/turnarounds/?token=
    path('', Documento.as_view(), name='documentos'),

    #POST: Agregar comentario a una subtarea del turnaround http://127.0.0.1:8000/documentos/comentario/?token=
    path('comentario/', ComentarioTurnaround.as_view(), name='comentario_turnaround'),

    #POST: Agregar hora inicio a una subtarea del turnaround http://127.0.0.1:8000/documentos/horainicio/?token=
    path('horainicio/', HoraInicioTurnaround.as_view(), name='horainicio_turnaround'),

    #POST: Agregar hora inicio y fin a una subtarea del turnaround http://127.0.0.1:8000/documentos/horainiciofin/?token=
    path('horainiciofin/', HoraInicioFinTurnaround.as_view(), name='horainiciofin_turnaround'),

    #POST: Agregar una imagen a subtarea del turnaround http://127.0.0.1:8000/documentos/imagen/?token=
    path('imagen/', ImagenTurnaround.as_view(), name='imagen_turnaround'),

    #GET: Buscar turnaround por ID con la infomación del vuelo y la plantilla asociada http://127.0.0.1:8000/documentos/tareas/<ID>/?token=
    path('tareas/<int:pk>/', TareasTurnaround.as_view(), name='tareas_lista'),

    #GET: Buscar turnaround por ID con la infomación del vuelo y la plantilla asociada http://127.0.0.1:8000/documentos/tareas/<ID>/?token=
    path('turnarounds/<int:pk>/', Turnarounds.as_view(), name='turnarounds'),

    path('turnarounds/horainiciofin/<int:pk>/', HoraInicioYFin.as_view(), name='hora_inicio_y_fin'),
]