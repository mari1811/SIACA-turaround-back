from rest_framework import serializers
from api.models import aerolinea
from django.contrib.auth import authenticate

#Serializador de todos los datos de la aerolinea
class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = aerolinea
        fields = '__all__'

