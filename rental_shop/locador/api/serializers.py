from rest_framework.serializers import ModelSerializer
from locador.models import Locador


class LocadorSerializer(ModelSerializer):
    class Meta:
        model = Locador
        fields = [
            'id', 'carrinho', 'usa_transportadora', 'endereco_entrega', 'endereco_devolucao']
