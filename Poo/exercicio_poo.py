"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    def _mostrar_dados(self):
        print(self._nome, self._cpf)

    @abstractmethod
    def _cadastro_cliente(self):
        self.cadastro = False
        return self.cadastro

class Cliente(Pessoa):

    def _mostrar_dados(self):
        print(self._nome, self._cpf, self.cadastro, self.tipo_conta)

    def _cadastro_cliente(self, nome_conta):
        self.tipo_conta = nome_conta
        self.cadastro = True
        
class Conta(ABC):
    def __init__(self):
        self._limite = 500
        self._limite_extra = 200

    @abstractmethod
    def _sacar(self, valor):...

    def mostrar_limite(self):
        print(self._limite)

class ContaCorrente(Conta):

    def tipo_conta(self):
        self.tipo_conta = "Conta Corrente"
        return self.tipo_conta

    def lim_extra(self):
        self._limite += self._limite_extra

    def mostrar_limite(self):
        print(f"Seu limite atual eh {self._limite} (Limite adicional de {self._limite_extra} incluido).")

    def _sacar(self, valor):
        self._limite -= valor
        print(f"Voce sacou {valor} reais")

class ContaPoupanca(Conta):

    def tipo_conta(self):
        self.tipo_conta = "Conta Poupanca"
        return self.tipo_conta
    
    def mostrar_limite(self):
        print(f"Seu limite atual eh {self._limite}.")

    def _sacar(self, valor):
        self._limite -= valor
        print(f"Voce sacou {valor} reais")


conta_corrente = ContaCorrente()
cliente1 = Cliente("Joao", 123456)
cliente1._cadastro_cliente(conta_corrente.tipo_conta())
print(f"O cliente {cliente1._nome}, CPF:{cliente1._cpf} possui a conta: {cliente1.tipo_conta}")

conta_poupanca = ContaPoupanca()
cliente2 = Cliente("Maria", 3626523172)
cliente2._cadastro_cliente(conta_poupanca.tipo_conta())
print(f"O cliente {cliente2._nome}, CPF:{cliente2._cpf} possui a conta: {cliente2.tipo_conta}")


