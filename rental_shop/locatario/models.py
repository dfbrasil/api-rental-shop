from usuario.models import Usuario
# from item.models import Item
# from locador.models import Locador
from endereco.models import Endereco
# from estoque.models import Estoque
from django.db import models
class Locatario(models.Model):

    nome_locatario = models.ForeignKey(
        Usuario,
        verbose_name= "Nome do locatário: ",
        on_delete = models.SET_NULL,
        blank=True,null=True,
    )

    def enviar_itens(self, estoque: 'Estoque') -> bool:
        entregou = False
        for item in estoque.get_lista_itens():
            if item.get_dono() == self and item.get_alugado() == True and item.get_disponivel() == False:
                item.set_entregue(True)
                entregou = True
        return entregou

    def __str__(self):
        return f'Nome: {self.nome_locatario.nome}\n'
