from rest_framework.serializers import ModelSerializer
from carrinho.models import Carrinho

class CarrinhoSerializer(ModelSerializer):

    class Meta:
        model = Carrinho
        fields = ['id','item_pedido','total','usa_transportadora','pago','entregue','devolvido','endereco_entrega','endereco_devolucao']