import pessoas
import contas

class Banco:
    def __init__(self, agencias: list[int] | None = None, clientes: list[pessoas.Pessoa] | None  = None, contas: list[contas.Conta] | None = None):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False
    
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False
    
    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False


    def autenticar(self, cliente: pessoas.Cliente, conta: contas.Conta):
        if self._checa_agencia(conta) and self._checa_cliente(cliente) and self._checa_conta(conta) and self._checa_se_conta_e_do_cliente(cliente, conta):
            return f"(Conta autenticada: agencia={self._checa_agencia(conta)}, cliente={self._checa_cliente(cliente)}, conta={self._checa_conta(conta)}, conta do cliente?={self._checa_se_conta_e_do_cliente(cliente, conta)})"
        return f"Conta NAO autenticada: agencia={self._checa_agencia(conta)}, cliente={self._checa_cliente(cliente)}, conta={self._checa_conta(conta)}, conta do cliente?={self._checa_se_conta_e_do_cliente(cliente, conta)})"

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"({self.agencias!r}, {self.clientes!r}, {self.contas!r})"
        return f"{class_name}{attrs}"

if __name__ == '__main__':

    cliente1 = pessoas.Cliente("Joao", 20)
    conta_corrente = contas.ContaCorrente("Nubank", 123)
    cliente1.conta = conta_corrente

    cliente2 = pessoas.Cliente("Maria", 56)
    conta_poupanca = contas.ContaPoupanca("PagBank", 456)
    cliente2.conta = conta_poupanca

    banco = Banco()
    banco.clientes.extend([cliente1])
    banco.contas.extend([conta_corrente])
    banco.agencias.extend(["Nubank"])

    print("################")

    print(f"{banco.autenticar(cliente1, conta_corrente)} -> {cliente1} - {conta_corrente}")
    print(banco)

    print("################")

    print(f"{banco.autenticar(cliente2, conta_poupanca)} -> {cliente2} - {conta_poupanca}")
    print(banco)

    print("################")

    if banco.autenticar(cliente1, conta_corrente):
        cliente1.conta.depositar(10)
        cliente1.conta.sacar(10)
        cliente1.conta.sacar(10)