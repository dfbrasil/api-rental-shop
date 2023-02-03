from django.db import models
from item.models import Item
from endereco.models import Endereco
from carrinho.models import Carrinho
from item_pedido.models import ItemPedido

class Locador(models.Model):

    carrinho = models.ForeignKey(
        Carrinho,
        verbose_name="Carrinho: ",
        on_delete = models.SET_NULL,
        blank=True, null= True,
    )

    usa_transportadora = models.BooleanField(
        default=False,
        verbose_name = "Usa Transportadora: ",
        blank=True, null=True,
    )

    endereco_entrega = models.ForeignKey(
        Endereco,
        on_delete=models.SET_NULL,
        verbose_name="Endereço para entrega: ",
        blank=True, null = True,
    )

    endereco_devolucao = models.ForeignKey(
        Endereco,
        on_delete=models.SET_NULL,
        verbose_name="Endereço para devolução: ",
        blank=True, null = True,
        related_name='+'
    )
    

    def get_carrinho(self) -> Carrinho:
        return self.__carrinho
    
    def set_carrinho(self, carrinho: Carrinho) -> None:
        self.__carrinho = carrinho
    
    def pagar_carrinho(self) -> None:
        if self.__carrinho.get_pago() == False:
            self.__carrinho.set_pago(True)
            return True
        else:
            return False
    
    def adicionar_item(self, item: Item, quantidade: int) -> bool:
        novo_item_pedido = ItemPedido(item, quantidade)
        self.__carrinho.set_itens_pedido(self.__carrinho.get_itens_pedido().append(novo_item_pedido))
        return True

    def remover_item(self, item: ItemPedido) -> bool:
        if item in self.__carrinho.get_itens_pedido():
            self.__carrinho.get_itens_pedido().remove(item)
            return True
        else:
            return False
