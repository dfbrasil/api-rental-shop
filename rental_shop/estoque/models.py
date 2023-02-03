from django.db import models
from item.models import Item


class Estoque(models.Model):

    def __init__(self):
        self.__lista_itens = list[Item]

    def get_lista_itens(self):
        return self.__lista_items

    def set_lista_items(self, new_lista_itens : list[Item]):
        self.__lista_itens = new_lista_itens
