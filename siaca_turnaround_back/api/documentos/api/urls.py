from django.urls import path
from .api import Documento
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    path('', Documento.as_view(), name='documentos')

]