from rest_framework import serializers
from api.models import maquinaria, categoria, maquinaria_historial, plantilla, vuelo, aerolinea, tarea, tipo, subtarea, turnaround, Hora
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

#Serializador datos de plantillas
class PlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = plantilla
        fields = '__all__'

#Serializador nombre de las aerolineas
class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = aerolinea
        fields = ('id', 'nombre')

#Serializador de datos de vuelo, plantilla y aerolinea asociados
class VueloSerializer(serializers.ModelSerializer):
    fk_plantilla = PlantillaSerializer()
    fk_aerolinea = AerolineaSerializer()
    class Meta:
        model = vuelo
        fields = ('numero_vuelo','id','fk_plantilla','fk_aerolinea')

#Serializador de tareas con su plantilla asociada
class TareaVistaSerializer(serializers.ModelSerializer):
    fk_plantilla = PlantillaSerializer()
    class Meta:
        model = tarea
        fields = '__all__'

#Serializador de tipo de tarea
class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo
        fields = '__all__'

#Serializador de plantilla con las tareas y subtareas asociadas
class PlantillaTareaSubtareaSerializer(serializers.ModelSerializer):
    fk_tarea = TareaVistaSerializer()
    fk_tipo = TipoSerializer()
    class Meta:
        model = subtarea
        fields = '__all__'

#Serializador de vuelos con sus aerolinaeas asociadas
class VueloInfoSerializer(serializers.ModelSerializer):
    fk_aerolinea = AerolineaSerializer()
    class Meta:
        model = vuelo
        fields = '__all__'

#Serializador de turnarounds con los datos de los vuelos y aerolineas asociados
class TurnaroundSerializer(serializers.ModelSerializer):
    fk_vuelo = VueloInfoSerializer()
    class Meta:
        model = turnaround
        fields = '__all__'

#Serializador hora de inicio
class HoraInicioSerializer(serializers.ModelSerializer):
    fk_subtarea = PlantillaTareaSubtareaSerializer()
    fk_turnaround = TurnaroundSerializer()
    class Meta:
        model = Hora
        fields = '__all__'

#Serializador hora de inicio y fin 
class HoraInicioFinSerializer(serializers.ModelSerializer):
    fk_subtarea = PlantillaTareaSubtareaSerializer()
    fk_turnaround = TurnaroundSerializer()
    class Meta:
        model = Hora
        fields = '__all__'