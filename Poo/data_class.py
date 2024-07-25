#Torna mais facil a criacao de classes
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

    def mostrar_info(self):
        print(f"NOME:{self.nome}\nIDADE:{self.idade}")

p1 = Pessoa("Joao", 20)
print(p1)
p1.nome = "Hugo"
print(p1.nome)
p1.mostrar_info()