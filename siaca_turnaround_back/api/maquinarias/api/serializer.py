from rest_framework import serializers
from api.models import maquinaria, maquinaria_turnaround, categoria, maquinaria_historial
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class MaquinariaTuraroundDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria_turnaround
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ('nombre','id')

class ListaCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'

class MaquinariaSerializer(serializers.ModelSerializer):
    fk_categoria = CategoriaSerializer()
    class Meta:
        model = maquinaria
        fields = '__all__'

class MaquinariaDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = '__all__'


class MaquinariaModificarSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = '__all__'

class ModificarSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = ('identificador','modelo')

class MaquinariaTuraroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria_turnaround
        fields = '__all__'

class MaquinariaEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = ('estado',)

class MaquinariaHistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria_historial
        fields = '__all__'

class MaquinariaCategoriaSerializer(serializers.ModelSerializer):

    fk_maquinaria = MaquinariaSerializer()
    class Meta:
        model = maquinaria_historial
        fields = '__all__'
