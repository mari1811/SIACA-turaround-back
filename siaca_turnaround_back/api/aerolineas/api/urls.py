from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .api import  Aerolinea, ModificarAerolinea
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[

    path('', Aerolinea.as_view(), name='lista_aerolineas'),
    path('<int:pk>/', ModificarAerolinea.as_view(), name='modificar_aerolineas')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)