from rest_framework import serializers
from .models import Tenis

class TenisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenis
        fields = ['id', 'name', 'type', 'brand']  # Define los campos que quieres incluir en el serializador
