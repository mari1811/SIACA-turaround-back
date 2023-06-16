from django.urls import path
from api.maquinarias.views import  MaquinariaAPIView


urlpatterns=[
    path('listado/',MaquinariaAPIView.as_view(), name='maquinarias'),
]