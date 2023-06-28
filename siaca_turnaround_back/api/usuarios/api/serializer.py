from rest_framework import serializers
from api.models import usuario
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password','username')

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        usuario_actualizado = super().update(instance,validated_data)
        usuario_actualizado.set_password(validated_data['password'])
        usuario_actualizado.save()
        return usuario_actualizado
    
class UsuarioListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')


class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DatosListaSerializer(serializers.ModelSerializer):
    fk_user = UsuarioListaSerializer()
    class Meta:
        model = usuario
        fields = '__all__'

class IDSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')