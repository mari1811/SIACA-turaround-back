from django.urls import path
from .api import Documento, ComentarioTurnaround, HoraInicioFinTurnaround, HoraInicioTurnaround, ImagenTurnaround, TareasTurnaround, Turnarounds, UpdateHora, UpdateHoraInicioFin, UpdateComentario, UpdateCodigoDemora
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

    #PATCH: Editar subtareas de tipo hora inicio con el id de la tarea http://127.0.0.1:8000/documentos/update-hora/<ID>/?token=
    path('update-hora/<int:pk>/', UpdateHora.as_view(), name='update_hora'),

    #PATCH: Editar subtareas de tipo hora inicio y fin con el id de la tarea http://127.0.0.1:8000/documentos/update-hora-inicio-fin/<ID>/?token=
    path('update-hora-inicio-fin/<int:pk>/', UpdateHoraInicioFin.as_view(), name='update_hora_inicio_fin'),

    #PATCH: Editar comentario con el id de la tarea http://127.0.0.1:8000/documentos/update-comentario/<ID>/?token=
    path('update-comentario/<int:pk>/', UpdateComentario.as_view(), name='update_comentario'),

    #PATCH: Editar codigo de demora con el id del turnaround http://127.0.0.1:8000/documentos/update-comentario/<ID>/?token=
    path('update-codigo/<int:pk>/', UpdateCodigoDemora.as_view(), name='update_codigo_demora'),
]