from rest_framework import serializers
from api.models import plantilla, tarea, subtarea
from django.contrib.auth import authenticate


class PlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tarea
        fields = '__all__'

class SubtareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = subtarea
        fields = ('titulo','tipo','fk_tarea')

class VistaPlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = ('titulo',)

class TareaVistaSerializer(serializers.ModelSerializer):
    fk_plantilla = VistaPlantillaSerializer()
    class Meta:
        model = tarea
        fields = ('fk_plantilla','titulo',)

class SubareaVistaSerializer(serializers.ModelSerializer):
    fk_tarea = TareaVistaSerializer()
    class Meta:
        model = subtarea
        fields = ('fk_tarea','titulo','tipo')



