from rest_framework import serializers
from api.models import turnaround, usuario_turnaround, maquinaria_turnaround, codigos_demora, vuelo, maquinaria
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class TurnaroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = turnaround
        fields = '__all__'

class CodigosSerializer(serializers.ModelSerializer):
    class Meta:
        model = codigos_demora
        fields = '__all__'

class MaquinariaTuraroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria_turnaround
        fields = '__all__'

class UsuarioTuraroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario_turnaround
        fields = '__all__'

class CodigosDemoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = codigos_demora
        fields = ('identificador','alpha')    

class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = vuelo
        fields = ('numero_vuelo',)    

class TurnaroundDetallesSerializer(serializers.ModelSerializer):
    fk_codigos_demora = CodigosDemoraSerializer()
    fk_vuelo = VueloSerializer()
    class Meta:
        model = turnaround
        fields = '__all__'

class MaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = '__all__'

class MaquinariaDetallesSerializer(serializers.ModelSerializer):
    fk_turnaround = TurnaroundDetallesSerializer()
    fk_maquinaria = MaquinariaSerializer()
    class Meta:
        model = maquinaria_turnaround
        fields = '__all__'

