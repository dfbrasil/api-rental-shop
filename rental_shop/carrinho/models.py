from django.db import models
from item_pedido.models import ItemPedido
from endereco.models import Endereco

class Carrinho(models.Model):

    item_pedido = models.ForeignKey(
        ItemPedido,
        on_delete=models.SET_NULL,
        verbose_name="Item Pedido: ",
        blank=True, null= True,
    )

    total = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name = "Total: ",
        blank=True, null= True,
    )

    usa_transportadora = models.BooleanField(
        default=False,
        verbose_name = "Usa Transportadora: ",
        blank=True, null=True,
    )

    pago = models.BooleanField(
        default=False,
        verbose_name = "Pago: ",
        blank=True, null=True,
    )

    entregue = models.BooleanField(
        default=False,
        verbose_name = "Entregue: ",
        blank=True, null=True,
    )

    devolvido = models.BooleanField(
        default=False,
        verbose_name = "Devolvido: ",
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

    def get_itens_pedido(self) -> list[ItemPedido]:
            return self.__itens_pedido
        
    def set_itens_pedido(self, itens_pedido: list[ItemPedido]) -> None:
        self.__itens_pedido = itens_pedido
    
    def get_total(self) -> float:
        return self.__total
    
    def set_total(self, total: float) -> None:
        self.__total = total

    def get_usa_transportadora(self) -> bool:
        return self.__usa_transportadora
    
    def set_usa_transportadora(self, usa_transportadora: bool) -> None:
        self.__usa_transportadora = usa_transportadora

    def get_pago(self) -> bool:
        return self.__pago
    
    def set_pago(self, pago: bool) -> None:
        self.__pago = pago

    def get_entregue(self) -> bool:
        return self.__entregue
    
    def set_entregue(self, entregue: bool) -> None:
        self.__entregue = entregue

    def get_devolvido(self) -> bool:
        return self.__devolvido
    
    def set_devolvido(self, devolvido: bool) -> None:
        self.__devolvido = devolvido

    def get_endereco_entrega(self) -> Endereco:
        return self.__endereco_entrega
    
    def set_endereco_entrega(self, endereco_entrega: Endereco) -> None:
        self.__endereco_entrega = endereco_entrega

    def get_endereco_devolucao(self) -> Endereco:
        return self.__endereco_devolucao
    
    def set_endereco_devolucao(self, endereco_devolucao: Endereco) -> None:
        self.__endereco_devolucao = endereco_devolucao
