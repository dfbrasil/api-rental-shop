from django.db import models
from usuario.models import Usuario
from item.models import Item
from estoque.models import Estoque
# from carrinho.models import Carrinho
# from item_pedido.models import ItemPedido

class Locador(models.Model):

    nome_locador = models.ForeignKey(
        Usuario,
        on_delete = models.SET_NULL,
        verbose_name="nome do locador",
        null=True,blank=True,    
    )

    # itens_escolhidos = models.ManyToManyField(
    #     'item.Item',
    #     blank=True,
    #     verbose_name= "lista de itens:",
    # )

    quantidade = models.PositiveIntegerField()

    produto = models.ManyToManyField(
        Item,
        verbose_name= "lista de itens:",
        blank=True,    
    )

    def get_itens_escolhidos(self) -> list['Item']:
        return self.__itens_escolhidos
    
    def set_itens_escolhidos(self, itens_escolhidos: list['Item']):
        self.__itens_escolhidos = itens_escolhidos

    def enviar_itens(self, ident: int, estoque: 'Estoque'):
        item_enviado = False
        for item in estoque.get_lista_itens():
            if item.get_ident() == ident and item.get_disponivel() == False and item.get_entregue() == True and item.get_alugado() == True:
                item.set_alugado(False)
                item.set_disponivel(True)
                item.set_entregue(False)
                item_enviado = True
        return item_enviado
            

    def adicionar_item(self, item: 'Item') -> bool:
        self.set_itens_escolhidos([*self.__itens_escolhidos, item])
        return True

    # locadores = Usuario.objects.filter(tipo='1')

    def __str__(self):
        return f'Nome: {self.nome_locador.nome}\n'