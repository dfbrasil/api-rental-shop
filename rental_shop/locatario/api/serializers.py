from rest_framework.serializers import ModelSerializer
from rental_shop.locatario.models import Locatario

class LocatarioSerializer(ModelSerializer):
    class Meta:
        model = Locatario
        fields = [
            'id', 'usuario'],
