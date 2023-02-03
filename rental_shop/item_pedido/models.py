from django.db import models
from item.models import Item

class ItemPedido(models.Model):

    item = models.ForeignKey(
        Item,
        on_delete = models.SET_NULL,
        verbose_name = "Item: ",
        blank = True, null = True,
    )

    quantidade = models.IntegerField(
        verbose_name = "Quantidade de itens: ",
        blank=True, null= True,
    )

    def get_item(self) -> str:
        return self.__item

    def set_item(self, novo_nome_item: Item) -> None:
        self.__item = Item(novo_nome_item)
    
    def get_quantidade(self) -> int:
        return self.__quantidade

    def set_quantidade(self, quantidade) -> None:
        self.__quantidade = quantidade

    def __str__(self) -> str:
        return (f'Item: {self.item}\nQuantidade: {self.quantidade}')