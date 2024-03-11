from rest_framework import serializers
from api.models import documento, vuelo, Hora, HoraInicioFin, Comentario, Imagen, turnaround, plantilla
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

#Serializador de vuelo con su plantilla
class VueloSerializer(serializers.ModelSerializer):
    fk_plantilla = PlantillaSerializer()
    class Meta:
        model = vuelo
        fields = '__all__'

#Serializador de turnaround con datos del vuelo y plantilla
class TurnaoundSerializer(serializers.ModelSerializer):
    fk_vuelo= VueloSerializer()
    class Meta:
        model = turnaround
        fields = '__all__'

#Serializador de turnaround con datos del vuelo y plantilla
class CodigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = turnaround
        fields = ("fk_codigos_demora_id",)

