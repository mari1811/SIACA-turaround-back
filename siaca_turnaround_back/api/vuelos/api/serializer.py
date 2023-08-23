from rest_framework import serializers
from api.models import vuelo, aerolinea, plantilla, ciudades, ciudades_destino, ciudades_salida, tipo_vuelo
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
        fields = '__all__'

class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudades
        fields = '__all__'

class CiudadesDestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudades_destino
        fields = '__all__'

class CiudadesSalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudades_salida
        fields = '__all__'

class TipoVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_vuelo
        fields = '__all__'


