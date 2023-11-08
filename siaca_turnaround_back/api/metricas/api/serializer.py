from rest_framework import serializers
from api.models import maquinaria, categoria, maquinaria_historial, plantilla, vuelo, aerolinea, tarea, tipo, subtarea, turnaround, Hora
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class PlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = '__all__'

class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = aerolinea
        fields = ('id', 'nombre')

class VueloSerializer(serializers.ModelSerializer):

    fk_plantilla = PlantillaSerializer()
    fk_aerolinea = AerolineaSerializer()
    class Meta:
        model = vuelo
        fields = ('numero_vuelo','id','fk_plantilla','fk_aerolinea')

class TareaVistaSerializer(serializers.ModelSerializer):
    fk_plantilla = PlantillaSerializer()
    class Meta:
        model = tarea
        fields = '__all__'

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo
        fields = '__all__'

class PlantillaTareaSubtareaSerializer(serializers.ModelSerializer):
    fk_tarea = TareaVistaSerializer()
    fk_tipo = TipoSerializer()
    class Meta:
        model = subtarea
        fields = '__all__'

class VueloInfoSerializer(serializers.ModelSerializer):
    fk_aerolinea = AerolineaSerializer()
    class Meta:
        model = vuelo
        fields = '__all__'

class TurnaroundSerializer(serializers.ModelSerializer):
    fk_vuelo = VueloInfoSerializer()
    class Meta:
        model = turnaround
        fields = '__all__'

class HoraInicioSerializer(serializers.ModelSerializer):
    fk_subtarea = PlantillaTareaSubtareaSerializer()
    fk_turnaround = TurnaroundSerializer()
    class Meta:
        model = Hora
        fields = '__all__'

class HoraInicioFinSerializer(serializers.ModelSerializer):
    fk_subtarea = PlantillaTareaSubtareaSerializer()
    fk_turnaround = TurnaroundSerializer()
    class Meta:
        model = Hora
        fields = '__all__'