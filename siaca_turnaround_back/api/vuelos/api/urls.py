from django.urls import path
from .api import vuelo_api_view, lista_api_vuelo, modificar_api_vuelos
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[

    path('', vuelo_api_view, name='vuelo_api_view'),
    path('lista/', lista_api_vuelo, name='lista_api_vuelo'),
    path('<int:pk>/', modificar_api_vuelos, name='modificar_api_vuelos')
]