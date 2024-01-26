from rest_framework import serializers
from api.models import vuelo, aerolinea, plantilla, ciudades, tipo_vuelo, tipo_servicio
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


#Serializador de todos los datos del vuelo
class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = vuelo
        fields = '__all__'

#Serializador nombre y ID de aerolinea
class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = aerolinea
        fields =('nombre','id')

#Serializador REG y ID de aerolinea 
class REGSerializer(serializers.ModelSerializer):
    class Meta:
        model = vuelo
        fields = ('ac_reg','fk_aerolinea_id')

#Serializador titulo de plantilla
class PlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = ('titulo',)

#Serializador lista de ciudades
class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudades
        fields = '__all__'

#Serializador  lista de tipos de vuelo
class TipoVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_vuelo
        fields = '__all__'

#Serializador lista de tipo de servicios
class TipoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_servicio
        fields = '__all__'

#Serializador vuelo con los datos completos 
class ListaVuelosSerializer(serializers.ModelSerializer):
    fk_aerolinea = AerolineaSerializer()
    fk_plantilla = PlantillaSerializer()
    stn = CiudadesSerializer()
    tipo_vuelo = TipoVueloSerializer()
    tipo_servicio = TipoServicioSerializer()
    lugar_destino = CiudadesSerializer()
    lugar_salida = CiudadesSerializer()

    class Meta:
        model = vuelo
        fields = '__all__'


