from rest_framework import serializers
from api.models import usuario
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password


class TokenUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('correo')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'

    def create(self,validated_data):
        user = usuario(**validated_data)
        user.contrasena = make_password(validated_data['contrasena'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        usuario_actualizado = super().update(instance,validated_data)
        usuario_actualizado.contrasena = make_password(validated_data['contrasena'])
        usuario_actualizado.save()
        return usuario_actualizado
    
class UsuarioListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('id', 'correo', 'contrasena')
