from rest_framework import serializers
from api.models import turnaround, usuario_turnaround, codigos_demora, vuelo, maquinaria, ciudades, aerolinea, tipo_vuelo, plantilla
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class TurnaroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = turnaround
        fields = '__all__'

class CodigosSerializer(serializers.ModelSerializer):
    class Meta:
        model = codigos_demora
        fields = '__all__'


class UsuarioTuraroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario_turnaround
        fields = '__all__'

class CodigosDemoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = codigos_demora
        fields = ('identificador','alpha')    

class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = vuelo
        fields = ('numero_vuelo',)   

class CiudadDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudades
        fields = '__all__'


class AerolineaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = aerolinea
        fields = '__all__'

class TipoVueloDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_vuelo
        fields = '__all__'

class PlantillaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = '__all__'

class VueloDetalleSerializer(serializers.ModelSerializer):
    stn = CiudadDetalleSerializer()
    fk_aerolinea = AerolineaDetalleSerializer()
    tipo_vuelo = TipoVueloDetalleSerializer()
    fk_plantilla = PlantillaDetalleSerializer()
    lugar_destino = CiudadDetalleSerializer()
    lugar_salida = CiudadDetalleSerializer()

    class Meta:
        model = vuelo
        fields = '__all__' 


class TurnaroundFechaSerializer(serializers.ModelSerializer):
    fk_codigos_demora = CodigosDemoraSerializer()
    fk_vuelo = VueloDetalleSerializer()
    
    class Meta:
        model = turnaround
        fields = '__all__'

class TurnaroundDetallesSerializer(serializers.ModelSerializer):
    fk_codigos_demora = CodigosDemoraSerializer()
    fk_vuelo = VueloSerializer()
    class Meta:
        model = turnaround
        fields = '__all__'

class MaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = '__all__'



