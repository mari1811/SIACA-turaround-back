from django.urls import path
from .api import plantilla_api_view, tarea_api_view, subtarea_api_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[

    path('', plantilla_api_view, name='plantilla_api_view'),
    path('tarea/', tarea_api_view, name='tarea_api_view'),
    path('subtarea/', subtarea_api_view, name='subtarea_api_view')
]

