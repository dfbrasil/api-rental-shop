from django.db import models
from locatario.models import Locatario


class Item(models.Model):
    
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

    dono = models.ForeignKey(
        Locatario,
        verbose_name="Dono do item",
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )

    alugado = models.BooleanField(
        verbose_name="Item alugado?",
        default=False,
        blank=True,null=True
    )

    entregue = models.BooleanField(
        verbose_name="Item entregue?",
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

    midia = models.ImageField(
        verbose_name = 'Fotos e Documentos',
        upload_to = 'imagens',
        blank = True, null = True,
    )


    def get_alugado(self) -> bool:
        return self.alugado
    
    def set_alugado(self, alugado: bool) -> None: 
        self.alugado = alugado

    def get_entregue(self) -> bool:
        return self.entregue

    def set_entregue(self, entregue: bool) -> None:
        self.entregue = entregue

    def get_disponivel(self) -> bool:
        return self.disponivel
    
    def set_disponivel(self, disponivel: bool) -> None:
        self.disponivel = disponivel

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome) -> None:
        self.nome = nome

    def get_preco(self) -> float:
        return self.preco

    def get_dono(self):
        return self.dono

    def set_dono(self, novo_dono) -> None:
        self.dono = novo_dono
               

    def __str__(self) -> str:
        return (f'Nome do Item: {self.nome} - Preço do Item: {self.preco} - Disponível: {self.quantidade}')

    # def __str__(self) -> str:
    #     return (f'ID: {self.id}\nNome do Item: {self.nome}\nPreço do Item: {self.preco}\nDono do Item: {self.dono.get_nome()}')

    