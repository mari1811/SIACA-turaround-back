from django.urls import path
from .api import usuario_api_view, usuarios_detalles_view
from api.usuarios.views import Login, Logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('listado/', usuario_api_view, name='usuario_api_view'),
    path('listado/<int:pk>/', usuarios_detalles_view, name='usuarios_detalles_view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]