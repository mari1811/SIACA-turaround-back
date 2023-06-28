from django.urls import path
from .api import usuario_api_view, usuarios_detalles_view, datos_api_view, UserListView
from api.usuarios.views import Login, Logout
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('registro/', usuario_api_view, name='usuario_api_view'),
    path('listado/datos/', datos_api_view, name='datos_api_view'),
    path('registro2usuario/<int:pk>/', datos_api_view, name='datos_api_view'),

    path('listado/user/', UserListView.as_view(), name='user_api_view'),

    path('registro2user/<int:pk>/', usuarios_detalles_view, name='usuarios_detalles_view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]