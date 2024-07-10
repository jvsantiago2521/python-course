#Atributos = Caracteristicas do objeto (Nome, cor, modelo, etc).
#Métodos = Ações do objeto (Andar, acelerar, correr, comer, atirar, etc.)

class Carro:
    def __init__(self, nome_carro, nome_motorista):
        #Uma função dentro de uma classe é um método
        #__init__ inicializa os atributos da classe
        #O self referencia o objeto em questão (p1 e p2)
        self.nome_carro = nome_carro
        self.nome_motorista = nome_motorista

    def acelerar(self, velocidade):
        print(f"{self.nome_motorista} está acelerando o {self.nome_carro} {velocidade}!")
    
etios = Carro("Etios", "João")
jac = Carro("Jac", "Sarah")

print(f"{etios.nome_motorista} tem um {etios.nome_carro}!")
print(f"{jac.nome_motorista} tem um {jac.nome_carro}!")
print("----------------------------------------------")
etios.acelerar("lentamente")
jac.acelerar("rapidamente")