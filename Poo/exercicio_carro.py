class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

class Motor:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro("Fusca")
volks = Fabricante("Volks")
motor_1_0 = Motor("1.0")
fusca.motor = motor_1_0
fusca.fabricante = volks

print(fusca.nome, fusca.motor.nome, fusca.fabricante.nome)



    