from rest_framework import serializers
from api.models import maquinaria, categoria, maquinaria_historial
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


#Serializador de categorias de maquinarias
class ListaCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

#Serializador de maquinarias con sus datos y sus categorias asociadas 
class MaquinariaSerializer(serializers.ModelSerializer):
    fk_categoria = ListaCategoriaSerializer()
    class Meta:
        model = maquinaria
        fields = '__all__'

#Serializador de maquinarias con sus datos
class MaquinariaDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = '__all__'

#DUPLICADO REVISAR 
class MaquinariaModificarSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = '__all__'

#Serializador para modificar las maquinarias 
class ModificarSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = ('identificador','modelo')

#Serializador para modoficar el estado de las maquinarias
class MaquinariaEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = ('estado',)

#Serializador historial de maquinarias (usos)
class MaquinariaHistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria_historial
        fields = '__all__'

#Serializador historial de maquinarias con información completa de la maquinaria 
class MaquinariaCategoriaSerializer(serializers.ModelSerializer):
    fk_maquinaria = MaquinariaSerializer()
    class Meta:
        model = maquinaria_historial
        fields = '__all__'
