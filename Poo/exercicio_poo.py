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

class Banco():
    def __init__(self):
        self._lista_clientes = []
        self._lista_contas = []
        self._lista_agencias = ["DF", "RJ", "SC"]

    def autenticar(self, entrada):
        if entrada.__class__.__name__ == "Cliente":
            self._lista_clientes.append(entrada)
            print(f"Cliente autenticado!")
        elif entrada.__class__.__name__ == "ContaPoupanca" or entrada.__class__.__name__ == "ContaCorrente":
            self._lista_contas.append(entrada)
            print(f"Conta autenticada!")
        else:
            print("Entrada invalida!")
       
    def verificar_autentificacao(self, entrada):
        if entrada in self._lista_clientes or entrada in self._lista_contas:
            print(f"Ja esta autentificado no sistema!")
            return True
        else:
            print("Autentificacao necessaria!")
            return False

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self._idade

class Cliente(Pessoa):
    def mostrar_info(self, entrada):
        print(entrada)


class Conta(ABC):
    def __init__(self, agencia, num_conta, saldo):
        self._agencia = agencia
        self._num_conta = num_conta
        self._saldo = saldo

    def _sacar(self):...

    def depositar(self):
        ...

class ContaCorrente(Conta):
    def _sacar(self):...

    def _saldo_com_extra(self):
        self._saldo += 300
        return self._saldo
    
class ContaPoupanca(Conta):
    def _sacar(self):...


santander = Banco()
cliente_joao = Cliente("Joao", 20)
conta_poupanca = ContaPoupanca("DF", 123, 239.80)

santander.autenticar(cliente_joao)
santander.autenticar(conta_poupanca)

cliente_joao.mostrar_info(conta_poupanca)
