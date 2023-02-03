from rest_framework.serializers import ModelSerializer
from rental_shop.item_pedido.models import ItemPedido


class ItemPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = [
            'id', 'item', 'quantidade']
