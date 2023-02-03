from rest_framework.viewsets import ModelViewSet
from item_pedido.models import ItemPedido
from .serializers import ItemPedidoSerializer


class ItemPedidoViewSet(ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer
    # filterset_fields = ['item']

