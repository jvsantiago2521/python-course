#Getter -> Obtem um valor
#Setter -> Configura um valor

class Caneta:
    def __init__(self, cor, marca, tampa):
        self.tampa = tampa
        self.marca = marca
        self.cor = cor

    @property
    def tampa(self):
        print("GET TAMPA")
        return self._tampa
            

    @property
    def cor(self):
        print("GET COR")
        return self._cor
    
    @property
    def marca(self):
        print("GET MARCA")
        return self._marca
    
    @cor.setter
    def cor(self, valor):
        if valor != "Azul":
            print("Essa cor não é valida")
            self._cor = "ERRO"
        else:
            self._cor = valor

    @marca.setter
    def marca(self, valor):
        print("SETTER")
        self._marca = valor

    @tampa.setter
    def tampa(self, valor):
        print("SETTER")
        self._tampa = valor

############################Codigo cliente############################

caneta = Caneta("Rosa", "Bic", "Redonda")
print(f"A caneta {caneta.cor}, da tampa {caneta.tampa}, é da marca {caneta.marca}")
caneta.cor = "Azul"
caneta.marca = "Faber Castell"
caneta.tampa = "Quadrada"
print(f"A caneta {caneta.cor}, da tampa {caneta.tampa}, é da marca {caneta.marca}")