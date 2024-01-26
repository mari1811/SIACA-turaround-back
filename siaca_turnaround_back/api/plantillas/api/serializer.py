from rest_framework import serializers
from api.models import plantilla, tarea, subtarea, categoria, cantidad_categoria, tipo, turnaround, Hora, HoraInicioFin
from django.contrib.auth import authenticate

def obtener_plantillas():
    plantillas = plantilla.objects.select_related('tarea__subtarea__fk_tipo').all()
    json_data = serializers.serialize('json', plantillas)
    return json_data

#Serializador información de plantillas 
class PlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = '__all__'

#Serializador de tareas
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tarea
        fields = '__all__'

#Serializador de subtareas
class SubtareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = subtarea
        fields = '__all__'

#Serializador tareas con sus plantillas asociadas 
class TareaVistaSerializer(serializers.ModelSerializer):
    fk_plantilla = PlantillaSerializer()
    class Meta:
        model = tarea
        fields = '__all__'

#Serializador subtareas con sus tareas y plantillas asociadas
class SubareaVistaSerializer(serializers.ModelSerializer):
    fk_tarea = TareaVistaSerializer()
    class Meta:
        model = subtarea
        fields = '__all__'

#Serializador categorias de maquinarias
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

#Serializador cantidad de maquinarias por categoria qeu requieren las plantillas
class CantidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = cantidad_categoria
        fields = '__all__'

#Serializador tipo de subtarea
class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo
        fields = '__all__'

#Serializador plantillas con la cantidad de maquinarias necesarias 
class PlantillaMaquinariaSerializer(serializers.ModelSerializer):
    fk_plantilla = PlantillaSerializer()
    fk_categoria = CategoriaSerializer()
    class Meta:
        model = cantidad_categoria
        fields = ('cantidad','fk_categoria','fk_plantilla')

#Serializador subtareas con su tipo y tarea asociada
class PlantillaTareaSubtareaSerializer(serializers.ModelSerializer):
    fk_tarea = TareaVistaSerializer()
    fk_tipo = TipoSerializer()
    class Meta:
        model = subtarea
        fields = '__all__'

#Serializador turnaround con toda su información
class TurnaroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = turnaround
        fields = '__all__'

#Serializador turnaround subtareas con su tipo y tarea asociada
class HoraInicioSerializer(serializers.ModelSerializer):
    fk_subtarea = PlantillaTareaSubtareaSerializer()
    fk_turnaround = TurnaroundSerializer()
    class Meta:
        model = Hora
        fields = '__all__'

