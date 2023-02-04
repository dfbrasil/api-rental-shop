from django.db import models
# from item.models import Item


class ItemPedido(models.Model):

    item = models.ForeignKey(
        'item.Item',
        on_delete = models.SET_NULL,
        verbose_name = "Item: ",
        blank = True, null = True,
    )

    qtd = models.IntegerField(
        verbose_name = "Quantidade de itens: ",
        blank=True, null= True,
    )

    # def get_item(self) -> str:
    #     return self.__item

    # def set_item(self, novo_nome_item: Item) -> None:
    #     self.__item = Item(novo_nome_item)
    
    def get_qtd(self) -> int:
        return self.__qtd

    def set_qtd(self, qtd) -> None:
        self.__qtd = qtd

    def __str__(self) -> str:
        return (f'Item: {self.item}\nQuantidade: {self.qtd}')
