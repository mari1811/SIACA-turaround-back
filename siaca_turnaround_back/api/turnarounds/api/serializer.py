from rest_framework import serializers
from api.models import turnaround, usuario_turnaround, maquinaria_turnaround, codigos_demora, vuelo, maquinaria, ciudades, ciudades_destino, ciudades_salida, aerolinea, tipo_vuelo, plantilla
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

class MaquinariaTuraroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria_turnaround
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

class CiudadDestinoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudades_destino
        fields = '__all__'

class CiudadSalidaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudades_salida
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
    lugar_salida = CiudadSalidaDetalleSerializer()
    lugar_destino = CiudadDestinoDetalleSerializer()
    stn = CiudadDetalleSerializer()
    fk_aerolinea = AerolineaDetalleSerializer()
    tipo_vuelo = TipoVueloDetalleSerializer()
    fk_plantilla = PlantillaDetalleSerializer()

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

class MaquinariaDetallesSerializer(serializers.ModelSerializer):
    fk_turnaround = TurnaroundDetallesSerializer()
    fk_maquinaria = MaquinariaSerializer()
    class Meta:
        model = maquinaria_turnaround
        fields = '__all__'

