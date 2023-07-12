from rest_framework import serializers
from api.models import aerolinea
from django.contrib.auth import authenticate


class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = aerolinea
        fields = '__all__'