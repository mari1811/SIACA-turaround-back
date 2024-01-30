from django.urls import path
from .api import Plantilla, Tarea, Subtarea, VistaPlantilla, VistaSubtarea, Maquinaria, VistaMaquinaria, Categoria, Tipo, ContadorMaquinaria, Plantillas
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[

    #GET: Lista de plantillas, POST: Crear plantilla  http://127.0.0.1:8000/plantillas/?token=
    path('', Plantilla.as_view(), name='lista_plantillas'),

    #POST: Crear una tarea http://127.0.0.1:8000/plantillas/tarea/?token=
    path('tarea/', Tarea.as_view(), name='lista_tareas'),

    #POST: Crear una tarea http://127.0.0.1:8000/plantillas/subtarea/?token=
    path('subtarea/', Subtarea.as_view(), name='lista_subtareas'),

    #POST: Agregar cantidad de maquinarias a una plantilla con su categoria http://127.0.0.1:8000/plantillas/maquinaria/?token=
    path('maquinaria/', Maquinaria.as_view(), name='lista_maquinaria'),

    #GET: Cantidad de maquinarias necesarias por plantilla especifica por ID http://127.0.0.1:8000/plantillas/maquinaria/<ID>/?token=
    path('maquinaria/<int:pk>/', VistaMaquinaria.as_view(), name='plantila_maquinaria'),

    #POST: Crear nueva categoria de maquinaria http://127.0.0.1:8000/plantillas/categoria/?token=
    path('categoria/', Categoria.as_view(), name='lista_categorias'),

    #GET: Lista de tipos de subtareas http://127.0.0.1:8000/plantillas/tipos/?token=
    path('tipos/', Tipo.as_view(), name='lista_tipos'),

    #GET: Tareas de una plantilla especifica por ID , DELETE: Eliminar plantilla espeficica por ID http://127.0.0.1:8000/plantillas/vista/<ID>/?token=
    path('vista/<int:pk>/', VistaPlantilla.as_view(), name='vista'),

    #GET: Todas las subtareas y tareas de una plantilla especifica por ID http://127.0.0.1:8000/plantillas/subtarea/<ID>/?token=
    path('subtarea/<int:pk>/', VistaSubtarea.as_view(), name='subtarea'),

    #GET: Contador de categorias de maquinarias http://127.0.0.1:8000/plantillas/contador/?token=
    path('contador/', ContadorMaquinaria.as_view(), name='contador'),

    #GET: Lista de todas las plantillas con todas sus tareas y subtareas http://127.0.0.1:8000/plantillas/plantillas/?token=
    path('plantillas/', Plantillas.as_view(), name='obtener_plantillas'),

]

