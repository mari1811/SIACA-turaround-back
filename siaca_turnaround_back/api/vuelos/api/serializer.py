from rest_framework import serializers
from api.models import vuelo, aerolinea, maquinaria, plantilla, usuario
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

class MaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = ('identificador',)

class PlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = ('titulo',)

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name')
        
class UsuarioSerializer(serializers.ModelSerializer):
    fk_user = DatosSerializer()
    class Meta:
        model = usuario
        fields = ('fk_user',)

class ListaVuelosSerializer(serializers.ModelSerializer):
    fk_aerolinea = AerolineaSerializer()
    fk_maquinaria = MaquinariaSerializer()
    fk_plantilla = PlantillaSerializer()
    fk_usuario = UsuarioSerializer()
    class Meta:
        model = vuelo
        fields = ('fk_aerolinea','fk_maquinaria','fk_plantilla','fk_usuario','ac_reg','lugar_salida','lugar_destino','fecha_llegada','hora_llegada','numero_vuelo','gate')

