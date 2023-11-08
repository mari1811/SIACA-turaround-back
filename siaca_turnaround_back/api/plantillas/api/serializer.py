from rest_framework import serializers
from api.models import plantilla, tarea, subtarea, categoria, cantidad_categoria, tipo, turnaround, Hora, HoraInicioFin
from django.contrib.auth import authenticate

def obtener_plantillas():
    plantillas = plantilla.objects.select_related('tarea__subtarea__fk_tipo').all()
    json_data = serializers.serialize('json', plantillas)
    return json_data


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
        fields = '__all__'

class VistaPlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = '__all__'

class TareaVistaSerializer(serializers.ModelSerializer):
    fk_plantilla = VistaPlantillaSerializer()
    class Meta:
        model = tarea
        fields = '__all__'

class SubareaVistaSerializer(serializers.ModelSerializer):
    fk_tarea = TareaVistaSerializer()
    class Meta:
        model = subtarea
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

class CantidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = cantidad_categoria
        fields = '__all__'

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo
        fields = '__all__'

class PlantillaMaquinariaSerializer(serializers.ModelSerializer):
    fk_plantilla = PlantillaSerializer()
    fk_categoria = CategoriaSerializer()
    class Meta:
        model = cantidad_categoria
        fields = ('cantidad','fk_categoria','fk_plantilla')

class PlantillaTareaSubtareaSerializer(serializers.ModelSerializer):
    fk_tarea = TareaVistaSerializer()
    fk_tipo = TipoSerializer()
    class Meta:
        model = subtarea
        fields = '__all__'

class TurnaroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = turnaround
        fields = '__all__'

class HoraInicioSerializer(serializers.ModelSerializer):
    fk_subtarea = PlantillaTareaSubtareaSerializer()
    fk_turnaround = TurnaroundSerializer()
    class Meta:
        model = Hora
        fields = '__all__'

