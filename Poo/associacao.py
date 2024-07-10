'''
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None


    @property
    def ferramenta(self):
        print("Getter")
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, valor):
        print("Setter")
        self._ferramenta = valor


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
    
    def escrever(self):
        return f"{self.nome} está escrevendo"

escritor = Escritor("João")
caneta = FerramentaDeEscrever("Caneta")
maquina = FerramentaDeEscrever("Maquina de escrever")
escritor.ferramenta = maquina
print(escritor.ferramenta.escrever())

'''

class Gamer:
    def __init__(self, nome):
        self.nome = nome
        self.jogo = None

    @property
    def jogo(self):
        return self._jogo
    
    @jogo.setter
    def jogo(self, valor):
        self._jogo = valor

class JogoParaJogar:
    def __init__(self, nome):
        self.nome = nome

    def mostrar_jogo(self):
        return f"{self.nome} está sendo jogado!"

gamer = Gamer("Alanzoka")
cod = JogoParaJogar("COD")
r6 = JogoParaJogar("R6")
gamer.jogo = r6
print(gamer.jogo.mostrar_jogo())