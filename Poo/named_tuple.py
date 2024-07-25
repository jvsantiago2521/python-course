#from collections import namedtuple
#Carta = namedtuple("Carta", ["valor", "naipe"],
#                   defaults=["VALOR PADRAO", "NAIPE PADRAO"])

from typing import NamedTuple

class Carta(NamedTuple):
    valor: str = "VALOR"
    naipe: str = "NAIPE"

carta_padrao = Carta()

print(carta_padrao)
print(carta_padrao.valor)
print(carta_padrao.naipe)

print()

as_espada = Carta("A","ESPADA")

print(as_espada)
print(as_espada.valor)
print(as_espada.naipe)

print()

print(as_espada._field_defaults)