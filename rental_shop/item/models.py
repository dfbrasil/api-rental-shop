from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from item_pedido.models import ItemPedido

# from item_pedido.models import ItemPedido


class Item(models.Model):
    # def __init__(self, ident: int, nome: str, preco: float, disponível: bool, dono: Locatario) -> None:
    # def __init__(self, ident: int, nome: str, preco: float, disponível: bool) -> None:
        
    nome = models.CharField(
        max_length=150,
        blank=True, null=True,
        verbose_name = "Nome do item",
    )

    quantidade = models.IntegerField(
        blank=True, null=True,
        verbose_name = "Quantidade de itens",
        default=0
    )

    preco = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name = "Preço do produto",
        blank=True, null=True,
    )

    disponivel = models.BooleanField(
        verbose_name="Item disponível?",
        default=False,
        blank=True,null=True
    )

    quantidade_pedida = models.IntegerField(
        blank=True, null=True,
        verbose_name = "Quantidade de itens pedidos",
    )

    quantidade_restante = models.IntegerField(
        blank=True, null=True,
        verbose_name = "Quantidade restatnte de itens",
    )


    def get_ident(self) -> int:
        return self.__id

    def set_ident(self, ident) -> None:
        self.__id = ident

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome) -> None:
        self.__nome = nome

    def get_preco(self) -> float:
        return self.__preco

    def get_dono(self) -> str:
        return self.__dono

    def set_dono(self, novo_nome_dono) -> None:
        self.__dono = Locatario(novo_nome_dono)


    import logging

    @receiver(post_save, sender=quantidade_pedida)
    def alterar_qts_itens(sender, instance, created, **kwargs):

        item = (Item.objects.get(pk=instance.item.id))

        try:
            if item.quantidade > 0:
                item.quantidade_restante -= item.quantidade - item.quantidade_pedida
                item.disponivel = True
                item.save()
            else:
                item.disponivel = False
                item.save()
            
        except BaseException:
            logging.exception("Quantidade solicidada maiorque a disponível!")






        #     return
        # except:
        #     return

        # qtd_solicitada = ItemPedido.objects.get(item=item).qtd
        # if qtd_solicitada <= item.quantidade:
        #         item.quantidade_restante = quantidade - qtd_solicitada
                

        
    # dono = models.ForeignKey(
    #     Locatario,
    #     verbose_name="Dono do item",
    #     on_delete=models.SET_NULL,
    #     blank=True, null=True,
    # )

    def __str__(self) -> str:
        return (f'Nome do Item: {self.nome} - Preço do Item: {self.preco} - Disponível: {self.quantidade}')

    