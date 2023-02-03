from rest_framework.serializers import ModelSerializer
from rental_shop.usuario.models import Usuario


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 'nome', 'cpf_cnpj', 'tipo', 'email', 'senha', 'logado', 'endereco']
