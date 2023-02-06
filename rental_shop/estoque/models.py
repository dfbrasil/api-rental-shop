from django.db import models
# from item.models import Item


class Estoque(models.Model):

    def __init__(self, lista_itens: list['Item']):
        
        lista_itens = models.ManyToManyField(
        Item,
        blank=True, null=True,
        verbose_name= "lista de itens:"
    )

    def __init__(self):
        self.__lista_itens = list[Item]

    def get_lista_itens(self):
        return self.__lista_items

    def set_lista_items(self, new_lista_itens : list['Item']):
        self.__lista_itens = new_lista_itens

    def cadastrar_item(self, nome: str, preco: float, disponivel: bool, alugado: bool, entregue: bool, dono) -> bool:
        new_item = Item(nome, preco, disponivel, alugado, entregue, dono)
        self.__lista_itens.append(new_item)
        return True

    def excluir_item(self, ident: int, dono) -> bool:
        for item in self.__lista_itens:
            if item.get_ident() == ident and item.get_dono() == dono:
                self.__lista_itens.remove(item)
                return True
        return False 