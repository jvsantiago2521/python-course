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
    
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
import pessoas
import banco
import contas

cliente1 = pessoas.Cliente("Joao", 20)
conta_corrente = contas.ContaCorrente("Nubank", 123)
cliente1.conta = conta_corrente

cliente2 = pessoas.Cliente("Maria", 56)
conta_poupanca = contas.ContaPoupanca("PagBank", 456)
cliente2.conta = conta_poupanca

banco = banco.Banco()
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