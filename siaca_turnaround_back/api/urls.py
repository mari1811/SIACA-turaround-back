from django.urls import path
from .views import MaquinariaView

urlpatterns=[
    path('maquinaria/',MaquinariaView.as_view(), name='maquinarias'),
    path('maquinaria/<int:id>',MaquinariaView.as_view(), name='maquina')
]