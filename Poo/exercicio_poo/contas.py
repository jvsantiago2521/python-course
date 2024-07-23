from abc import ABC, abstractmethod

class Conta(ABC):
    #Contas têm agência, número da conta e saldo
    #Contas devem ter método para depósito
    #Conta (super classe) deve ter o método sacar abstrato (Abstração e polimorfismo - as subclasses que implementam o método sacar)

    def __init__(self, agencia: str, num_conta: int, saldo: float = 0):
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float:...
    
    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f"[DEPOSITO: +{valor:.2f}]")
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f"SALDO: {self.saldo:.2f} {msg}")
        print("------")

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencia!r}, {self.num_conta!r}, {self.saldo!r})"
        return f"{class_name}{attrs}"


#Criar classes ContaPoupanca e ContaCorrente que herdam de Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        self.valor_pos_saque = self.saldo - valor

        if self.valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f"[SAQUE: -{valor}]")
            return self.saldo
        
        print("Nao foi possivel efetuar o saque")
        self.detalhes(f"[SAQUE NEGADO: {valor:.2f}]")

class ContaCorrente(Conta):
    #ContaCorrente deve ter um limite extra
    def __init__(self, agencia: str, num_conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        self.valor_pos_saque = self.saldo - valor
        lim_max = -self.limite

        if self.valor_pos_saque >= lim_max:
            self.saldo -= valor
            self.detalhes(f"[SAQUE: -{valor:.2f}]")
            return self.saldo

        print("Nao foi possivel efetuar o saque")
        self.detalhes(f"[LIMITE: {lim_max:.2f}]")
        self.detalhes(f"[SAQUE NEGADO: {valor:.2f}]")
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencia!r}, {self.num_conta!r}, {self.saldo!r}, {self.limite!r})"
        return f"{class_name}{attrs}"
    
if __name__ == '__main__':

    conta_poupanca1 = ContaPoupanca("Santander", 2521)
    conta_poupanca1.depositar(10)
    conta_poupanca1.sacar(30)
    conta_poupanca1.depositar(100)
    conta_poupanca1.sacar(50)

    print("#########")

    conta_corrente1 = ContaCorrente("Nubank", 9484, 0, 100)
    conta_corrente1.depositar(10)
    conta_corrente1.sacar(30)
    conta_corrente1.depositar(100)
    conta_corrente1.sacar(50)
    conta_corrente1.sacar(50)
    conta_corrente1.sacar(100)

