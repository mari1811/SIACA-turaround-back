from rest_framework import serializers
from api.models import usuario
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from api.models import usuario, usuario_turnaround, turnaround, cargo, departamento

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password','username', 'is_active')

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
        fields = ('username','first_name','last_name')

class EstadoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('is_active',)

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UpdateUserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UpdateSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name')

class IDSolicitudes(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)
        
class DatosListaSerializer(serializers.ModelSerializer):
    fk_user = UpdateUserSeralizer()
    class Meta:
        model = usuario
        fields = '__all__'

class UpdateUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'

class IDSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)

class TurnaroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = turnaround
        fields = '__all__'

class UsuarioDatosTurnaroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario_turnaround
        fields = '__all__'

class UsuarioTurnaroundSerializer(serializers.ModelSerializer):
    fk_usuario = DatosListaSerializer()
    fk_turnaround = TurnaroundSerializer()
    class Meta:
        model = usuario_turnaround
        fields = '__all__'




class EmailSerializer(serializers.Serializer):
    """
    Reset Password Email Request Serializer.
    """

    email = serializers.EmailField()

    class Meta:
        fields = ("email",)



class ResetPasswordSerializer(serializers.Serializer):
    """
    Reset Password Serializer.
    """

    password = serializers.CharField(
        write_only=True,
        min_length=1,
    )

    class Meta:
        field = ("password")

    def validate(self, data):
        """
        Verify token and encoded_pk and then set new password.
        """
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")

        if token is None or encoded_pk is None:
            raise serializers.ValidationError("Missing data.")

        pk = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(pk=pk)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid")

        user.set_password(password)
        user.save()
        return data