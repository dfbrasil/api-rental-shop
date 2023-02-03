from rest_framework.viewsets import ModelViewSet
from carrinho.models import Carrinho
from .serializers import CarrinhoSerializer

class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    # filterset_fields = ['id','item_pedido']