from rest_framework import serializers
from api.models import maquinaria

class MaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinaria
        fields = '__all__'