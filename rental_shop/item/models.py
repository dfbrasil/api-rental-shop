from django.db import models

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

    quantidade_restante = models.IntegerField(
        blank=True, null=True,
        verbose_name = "Quantidade de itens restantes",
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

    # dono = models.ForeignKey(
    #     Locatario,
    #     verbose_name="Dono do item",
    #     on_delete=models.SET_NULL,
    #     blank=True, null=True,
    # )

    class ItemPedido(models.Model):

        item = models.ForeignKey(
            'item.Item',
            on_delete = models.SET_NULL,
            verbose_name = "Item: ",
            blank = True, null = True,
            related_name = "+"
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


    
        
        
        def calcular_quantidade_restante(self):
            try:
                qtd_pedida = ItemPedido.objects.get().qtd
                if qtd_pedida <= self.quantidade:
                    self.quantidade_restante = self.quantidade - qtd_pedida
                    self.save()
                return self.quantidade_restante
            except:
                return print("Quantidade pedida é maior que a quantidade do estoque.")
        

    def __str__(self) -> str:
        return (f'Nome do Item: {self.nome} - Preço do Item: {self.preco} - Disponível: {self.quantidade_restante}')

    