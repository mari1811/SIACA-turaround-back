from rest_framework import serializers
from api.models import vuelo, aerolinea, plantilla
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = vuelo
        fields = '__all__'

class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = aerolinea
        fields =('nombre',)

class PlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = ('titulo',)
        
class ListaVuelosSerializer(serializers.ModelSerializer):
    fk_aerolinea = AerolineaSerializer()
    fk_plantilla = PlantillaSerializer()

    class Meta:
        model = vuelo
        fields = ('fk_aerolinea','fk_plantilla','ac_reg','lugar_salida','lugar_destino','fecha_llegada','hora_llegada','numero_vuelo','gate')




