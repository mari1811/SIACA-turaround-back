from rest_framework import serializers
from api.models import maquinaria, maquinaria_turnaround
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class MaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = '__all__'

