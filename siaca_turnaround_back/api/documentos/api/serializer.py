from rest_framework import serializers
from api.models import documento, vuelo, Hora, HoraInicioFin, Comentario, Imagen, turnaround, plantilla, aerolinea, tipo_servicio, tipo_vuelo, ciudades, codigos_demora
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


#Serializador de todos los datos de documentos
class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = documento
        fields = '__all__'

#Serializardor de número de vuelo
class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = vuelo
        fields = ('numero_vuelo',)

#Serializador documento con su número de vuelo asociado
class DocumentosDatosSerializer(serializers.ModelSerializer):
    fk_vuelo = VueloSerializer()
    class Meta:
        model = documento
        fields = '__all__'

#Serializador de subtarea HORA
class HoraInicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hora
        fields = '__all__'

#Serializador de subtarea HORA INICIO Y FIN
class HoraInicioFinSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoraInicioFin
        fields = '__all__'

#Serializador de subtarea COMENTARIO
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

#Serializador de subtarea IMAGEN
class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'

#Serializador de todos los datos de PLANTILLA
class PlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = '__all__'

#Serializador de todos los datos de AEROLINEA
class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = aerolinea
        fields = '__all__'

#Serializador de todos los datos de TIPO SERVICIO
class TipoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_servicio
        fields = '__all__'

#Serializador de todos los datos de TIPO DE VUELO
class TipoVueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_vuelo
        fields = '__all__'

#Serializador de todos los datos de CIUDADES
class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudades
        fields = '__all__' 


#Serializador de todos los datos de CODIGO DE DEMORA
class CodigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = codigos_demora
        fields = '__all__' 


#Serializador de vuelo con TODOS LOS DATOS
class VueloSerializer(serializers.ModelSerializer):
    fk_plantilla = PlantillaSerializer()
    fk_aerolinea = AerolineaSerializer()
    tipo_vuelo = TipoVueloSerializer()
    tipo_servicio = TipoServicioSerializer()
    stn_id = CiudadesSerializer()
    lugar_salida = CiudadesSerializer()
    lugar_destino = CiudadesSerializer()
    class Meta:
        model = vuelo
        fields = '__all__'

#Serializador de turnaround con datos del vuelo y plantilla
class TurnaoundSerializer(serializers.ModelSerializer):
    fk_vuelo= VueloSerializer()
    fk_codigos_demora = CodigoSerializer()
    class Meta:
        model = turnaround
        fields = '__all__'

#Serializador de turnaround con datos del vuelo y plantilla
class CodigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = turnaround
        fields = ("fk_codigos_demora_id",)

