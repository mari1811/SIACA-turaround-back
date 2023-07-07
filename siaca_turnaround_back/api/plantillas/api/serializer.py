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


