from django.db import models
from endereco.models import Endereco
from carrinho.models import Carrinho

class Transportadora(models.Model):

    nome = models.CharField(
        max_length=50,
        verbose_name = "Transportadora: ",
        blank=True, null = True,
    )

    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.SET_NULL,
        verbose_name="Endereço: ",
        blank=True, null=True,   
    )

    carrinho = models.ForeignKey(
        Carrinho,
        on_delete=models.SET_NULL,
        verbose_name="Carrinho: ",
        blank=True, null=True,
    )

    def get_nome(self) -> str:
            return self.__nome
        
    def set_nome(self, new_nome: str) -> None:
            self.__nome = new_nome
    
    def get__carrinhos(self) -> Carrinho:
        return self.__carrinhos

    def set__carrinhos(self, new_carrinhos: list[Carrinho]) -> None:
        self.__carrinhos = new_carrinhos

    def transportar(self, carrinho : Carrinho):
        print(carrinho.set_entregue(True)) # por enquanto...

    def __str__(self):
        return f'Nome: {self.__nome}'

