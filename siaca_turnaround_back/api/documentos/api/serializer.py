from rest_framework import serializers
from api.models import documento, vuelo, Hora, HoraInicioFin, Comentario, Imagen, turnaround, plantilla
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

class HoraInicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hora
        fields = '__all__'

class HoraInicioFinSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoraInicioFin
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'

class PlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = '__all__'

class VueloSerializer(serializers.ModelSerializer):
    fk_plantilla = PlantillaSerializer()
    class Meta:
        model = vuelo
        fields = '__all__'

class TurnaoundSerializer(serializers.ModelSerializer):
    fk_vuelo= VueloSerializer()
    class Meta:
        model = turnaround
        fields = '__all__'

