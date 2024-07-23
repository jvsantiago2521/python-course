import contas

class Pessoa():
#Pessoa tem nome e idade (com getters)
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.nome!r}, {self.idade!r})"
        return f"{class_name}{attrs}"


#Criar classe Cliente que herda da classe Pessoa (Herança)
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        #Tipagem como: Pode ser do tipo conta ou None
        #Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
        self.conta: contas.Conta | None = None
        

if __name__ == '__main__':

    cliente1 = Cliente("Joao", 20)
    #Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
    cliente1.conta = contas.ContaPoupanca("Nubank", 1234)

    cliente2 = Cliente("Maria", 45)
    #Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
    cliente2.conta = contas.ContaCorrente("Santander", 4321, 0, 250)

    print(f"{cliente1} -> {cliente1.conta}")

    cliente1.conta.depositar(10)
    cliente1.conta.sacar(20)

    print(f"{cliente2} -> {cliente2.conta}")

    cliente2.conta.depositar(10)
    cliente2.conta.sacar(20)
    cliente2.conta.sacar(240)
    cliente2.conta.sacar(1)
