from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .api import  Aerolinea, ModificarAerolinea
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[
    #GET: Lista de aerolineas , POST: Crear nueva aerolinea http://127.0.0.1:8000/aerolineas/?token=
    path('', Aerolinea.as_view(), name='lista_aerolineas'), 

    #GET: Buscar aerolinea por ID, PATCH: Modificar aerolinea por ID, DELETE: Eliminar aerolinea por ID http://127.0.0.1:8000/aerolineas/<ID>/?token=
    path('<int:pk>/', ModificarAerolinea.as_view(), name='modificar_aerolineas'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)