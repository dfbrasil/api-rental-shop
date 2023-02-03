from rest_framework.serializers import ModelSerializer
from rental_shop.transportadora.models import Transportadora


class TransportadoraSerializer(ModelSerializer):
    class Meta:
        model = Transportadora
        fields = [
            'id', 'nome', 'endereco', 'carrinho']
