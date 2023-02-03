from rest_framework.serializers import ModelSerializer
from locatario.models import Locatario

class LocatarioSerializer(ModelSerializer):
    class Meta:
        model = Locatario
        fields = [
            'id', 'usuario'],
