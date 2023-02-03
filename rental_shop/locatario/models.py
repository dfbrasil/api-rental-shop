from django.db import models
from item.models import Item
from usuario.models import Usuario
from locador.models import Locador
from carrinho.models import Carrinho

class Locatario(models.Model):

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        verbose_name="Usuaŕio: ",
        blank=True, null=True,
    )

    def cadastrar_item(self, ident : int, nome : str, preco : float, disponivel : bool) -> Item:
        new_item = Item(ident, nome, preco, disponivel, self)
        self.list_itens_locatario.append(new_item)  # adicionar na lista
        return new_item

    def excluir_item(self, ident : int) -> None: # remover da lista
        for item in range(self.list_itens_locatario):
            if item.get_ident == ident:
                self.list_itens_locatario.remove(item)

    def enviar_itens(self, carrinho : Carrinho):
        carrinho.set_entregue(True)
        print("realizou a entrega do ", carrinho)

    def ver_itens(self):
        for item in range(self.list_itens_locatario):
            print(item.get_nome())

    def __str__(self):
        return f'Nome: {self.get_nome}\n'
