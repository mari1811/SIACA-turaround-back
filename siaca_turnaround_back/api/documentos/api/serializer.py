from rest_framework import serializers
from api.models import documento, vuelo
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = documento
        fields = '__all__'

class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = vuelo
        fields = ('numero_vuelo',)

class DocumentosDatosSerializer(serializers.ModelSerializer):
    fk_vuelo = VueloSerializer()
    class Meta:
        model = documento
        fields = '__all__'