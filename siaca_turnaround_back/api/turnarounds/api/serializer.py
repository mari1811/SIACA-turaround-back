from rest_framework import serializers
from api.models import turnaround, usuario_turnaround, maquinaria_turnaround
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class TurnaroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = turnaround
        fields = '__all__'

