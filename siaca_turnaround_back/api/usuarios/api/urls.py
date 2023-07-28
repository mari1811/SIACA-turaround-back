from django.urls import path
from .api import usuario_api_view, usuarios_detalles_view, datos_api_view, UserListView, registro_usuario, Lista, Prueba, Update
from api.usuarios.views import Login, Logout, PasswordReset, ResetPasswordAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('registro/', usuario_api_view, name='usuario_api_view'),
    path('lista/', Lista.as_view(), name='lista'),
    path('listado/datos/', datos_api_view, name='datos_api_view'),
    path('registro2usuario/<int:pk>/', datos_api_view, name='datos_api_view'),
    path('registro2usuario/', registro_usuario, name='registro_usuario'),

    path('listado/user/', UserListView.as_view(), name='user_api_view'),
    path('registro2user2/<int:pk>/', Update.as_view(), name='update'),

    path('registro2user/<int:pk>/', usuarios_detalles_view, name='usuarios_detalles_view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password-reset/', PasswordReset.as_view(), name ="request-password-reset"),
    path('password-reset/<str:encoded_pk>/<str:token>', ResetPasswordAPI.as_view(), name ="reset-password"),

    path('prueba/', Prueba.as_view(), name='prueba'),
]