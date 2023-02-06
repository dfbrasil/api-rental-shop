from django.db import models

class Endereco(models.Model):

   

    logradouro = models.CharField(
        max_length=200,
        verbose_name="Rua/Avenida: ",
        blank=True, null=True,
    )

    cidade = models.CharField(
        max_length=50,
        verbose_name="Cidade: ",
        blank=True, null=True,
    )

    estado = models.CharField(
        max_length=50,
        verbose_name="Estado: ",
        blank=True, null=True,
    )

    pais = models.CharField(
        max_length=50,
        verbose_name="País: ",
        blank=True, null=True,
    )

    def get_logradouro(self) -> str:
        return self.__logradouro
    
    def set_logradouro(self,logradouro) -> None:
        self.__logradouro = logradouro

    def get_cidade(self) -> str:
        return self.__cidade
    
    def set_cidade(self, cidade) -> None:
        self.__cidade = cidade

    def get_estado(self) -> str:
        return self.__estado

    def set_estado(self, estado) -> None:
        self.__estado = estado

    def get_pais(self) -> str:
        return self.__pais

    def set_pais(self, pais) -> None:
        self.__pais = pais

    def __str__(self) -> str :
        return (f'Logradouro: {self.logradouro}\nCidade: {self.cidade}\nEstado: {self.estado} \n{self.pais}')

