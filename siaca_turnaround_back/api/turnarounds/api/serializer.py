from rest_framework import serializers
from api.models import turnaround, usuario_turnaround, codigos_demora, vuelo, maquinaria, ciudades, aerolinea, tipo_vuelo, plantilla, tipo_servicio
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

#Serializador de turnaround con todos los datos 
class TurnaroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = turnaround
        fields = '__all__'

#Serializador de codigos de demora de los vuelos infromación completa 
class CodigosSerializer(serializers.ModelSerializer):
    class Meta:
        model = codigos_demora
        fields = '__all__'

#Serializador de historial de personal en los turarounds 
class UsuarioTuraroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario_turnaround
        fields = '__all__'

#Serializador codigos de demora de los vuelos solo identificador y alpha
class CodigosDemoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = codigos_demora
        fields = '__all__'   

#Serializador solo número de los vuelos
class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = vuelo
        fields = '__all__'  

#Serializador lista de ciudades información completa
class CiudadDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudades
        fields = '__all__'

#Serializador lista de aerolineas información completa
class AerolineaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = aerolinea
        fields = '__all__'

#Serializador lista de los tipos de vuelos
class TipoVueloDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_vuelo
        fields = '__all__'

#Serializador lista de los tipos de vuelos
class TipoServicioDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_servicio
        fields = '__all__'

#Serializador lista de plantillas 
class PlantillaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = '__all__'

#Serializador lista de vuelos con toda su información completa
class VueloDetalleSerializer(serializers.ModelSerializer):
    stn = CiudadDetalleSerializer()
    fk_aerolinea = AerolineaDetalleSerializer()
    tipo_vuelo = TipoVueloDetalleSerializer()
    tipo_servicio = TipoServicioDetalleSerializer()
    fk_plantilla = PlantillaDetalleSerializer()
    lugar_destino = CiudadDetalleSerializer()
    lugar_salida = CiudadDetalleSerializer()

    class Meta:
        model = vuelo
        fields = '__all__' 

#Serializador turnaround con codigo de demora e información completa del vuelo
class TurnaroundDetallesSerializer(serializers.ModelSerializer):
    fk_codigos_demora = CodigosDemoraSerializer()
    fk_vuelo = VueloDetalleSerializer()
    class Meta:
        model = turnaround
        fields = '__all__'

#Serializador lista de maquinarias 
class MaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = '__all__'




