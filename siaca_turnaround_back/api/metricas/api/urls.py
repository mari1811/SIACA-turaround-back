from django.urls import path
from .api import   MetricaUsoMaquinaria, MetricaTurnaroundPersonal, MetricaTurnaroundAerolineas, MetricaTurnaroundSLA
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    path('maquinarias/', MetricaUsoMaquinaria.as_view(), name='metrica_maquinarias'),
    path('personal/', MetricaTurnaroundPersonal.as_view(), name='metrica_personal'),
    path('aerolineas/', MetricaTurnaroundAerolineas.as_view(), name='metrica_aerolineas'),
    path('SLA/', MetricaTurnaroundSLA.as_view(), name='metrica_SLA'),
]