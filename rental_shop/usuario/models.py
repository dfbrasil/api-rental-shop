from django.db import models
from endereco.models import Endereco


class Usuario(models.Model):

    

    nome = models.CharField(
        max_length=150,
        verbose_name = "Nome: ",
        blank=True, null= True,
    )

    cpf_cnpj = models.IntegerField(
        verbose_name="Cpf ou CNPJ: ",
        blank=True, null= True,
    )

    CHOICES_TIPO = (
        ('1', 'Locador'),
        ('2', 'Locatário'),
    )

    tipo = models.CharField(
        verbose_name='Tipo do Usuário',
        choices=CHOICES_TIPO,
        max_length=20,
        blank=True, null=True,
    )

    email = models.CharField(
        max_length=50,
        verbose_name = "Email: ",
    )

    senha = models.CharField(
        max_length= 20,
        verbose_name = "Senha: ",
    )

    logado = models.BooleanField(
        default=False,
        verbose_name = "Usuário Logado: ",
        blank=True, null=True,
    )

    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.SET_NULL,
        verbose_name="Endereço do usuário: ",
        blank=True, null= True,
    )

    """
        Método logar - autenticação do usuário; 
        Recebe email e senha como parâmetros;
        Retorna True se o usuário conseguir logar, caso contrário retorna False.    
    """

    def logar(self, email, senha) -> bool:
        if self.get_email() == email and self.get_senha() == senha:
            self.__logado = True
            return True
        else:
            return False

    """
        Método enviar_itens - método abstrato que é implementado por Locador e Locatário
        Encaminha o(s) item/itens para a entrega
        Caso seja chamado pelo locador, realiza a devolução do item
        Caso seja chamado pelo locatário, realiza a entrega para empréstimo do item
    """

    # VER SE RECEBE O CARRINHO COMO PARÂMETRO MESMO. SE SIM, MUDAR NO DIAGRAMA
    def enviar_itens(self):
        # implementar aqui
        pass

    """ getters e setters """

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome) -> None:
        self.__nome = nome

    def get_cpf_ou_cnpj(self) -> str:
        return self.__cpf_ou_cnpj

    def set_cpf_ou_cnpj(self, cpf_ou_cnpj) -> None:
        self.__cpf_ou_cnpj = cpf_ou_cnpj

    def get_tipo(self) -> int:
        return self.__tipo

    def set_tipo(self, tipo) -> None:
        self.__tipo = tipo

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email) -> None:
        self.__email = email

    def get_senha(self) -> str:
        return self.__senha

    def set_senha(self, senha) -> None:
        self.__senha = senha

    def get_logado(self):
        return self.__logado

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco) -> None:
        self.__endereco = endereco

    def __str__(self) -> str:
        return (f"Usuário: {self.__nome}\nCPF/CNPJ: {self.__cpf_ou_cnpj}\nTipo: {self.__tipo}\nEmail: {self.__email}\nSenha: {self.__senha}\nEndereço: {self.__endereco} ")
