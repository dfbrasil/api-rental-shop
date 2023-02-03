from rest_framework.serializers import ModelSerializer
from item_pedido.models import ItemPedido


class ItemPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = [
            'id', 'item', 'quantidade']
