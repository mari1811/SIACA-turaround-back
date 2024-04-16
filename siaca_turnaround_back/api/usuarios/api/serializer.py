from rest_framework import serializers
from api.models import usuario
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from api.models import usuario, usuario_turnaround, turnaround, cargo, departamento, vuelo, aerolinea, rol

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode


#Serializador de user para crear usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password','username', 'is_active')

    #Crea usuario y cifra la clave
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    #Actualiza datos del usuario
    def update(self, instance, validated_data):
        usuario_actualizado = super().update(instance,validated_data)
        usuario_actualizado.set_password(validated_data['password'])
        usuario_actualizado.save()
        return usuario_actualizado

 #Serializador correo, nombre y apellido
class UsuarioListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name')

#Serializador para asignar rol
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('fk_rol_id',)

#Serializador para activar el usuario
class EstadoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('is_active',)

#Serializador para activar el usuario
class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario_turnaround
        fields = ('asistencia',)

#Serializador datos completos de la tabla User
class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#Serializador lista de cargos
class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = cargo
        fields = '__all__' 

#Serializador lista de departamentos     
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = departamento
        fields = '__all__' 

#Serializador nombre y apellido
class UpdateSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name')


#Serializador rol
class RolSeralizer(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = '__all__'

#Serializador usuario con todos los datos     
class DatosListaSerializer(serializers.ModelSerializer):
    fk_user = DatosSerializer()
    fk_departamento = DepartamentoSerializer()
    fk_cargo = CargoSerializer()
    fk_rol = RolSeralizer()
    class Meta:
        model = usuario
        fields = '__all__'

#Serializador tabla usuario
class UpdateUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'

#Serializador id de User
class IDSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)

class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = aerolinea
        fields = '__all__'

class VuelosSerializer(serializers.ModelSerializer):
    fk_aerolinea = AerolineaSerializer()
    class Meta:
        model = vuelo
        fields = '__all__'

#Serializador turnarounds 
class TurnaroundSerializer(serializers.ModelSerializer):
    fk_vuelo = VuelosSerializer()
    class Meta:
        model = turnaround
        fields = '__all__'

#Serializador historial del personal en los turnarounds 
class UsuarioDatosTurnaroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario_turnaround
        fields = '__all__'


#Serializador historial de personal en turnarounds con datos completos 
class UsuarioTurnaroundSerializer(serializers.ModelSerializer):
    fk_usuario = DatosListaSerializer()
    fk_turnaround = TurnaroundSerializer()
    class Meta:
        model = usuario_turnaround
        fields = '__all__'
        
#Serializador historial de personal en turnarounds con datos del personal
class DepartamentoUsuarioListaSerializer(serializers.ModelSerializer):
    fk_usuario = DatosListaSerializer()
    class Meta:
        model = usuario_turnaround
        fields = '__all__'


#Serializador para enviar correo de recuperación de clave
class EmailSerializer(serializers.Serializer):
    """
    Reset Password Email Request Serializer.
    """

    email = serializers.EmailField()

    class Meta:
        fields = ("email",)


#Serializador para recuperación de clave
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
            raise serializers.ValidationError("Token no válido")

        user.set_password(password)
        user.save()
        return data