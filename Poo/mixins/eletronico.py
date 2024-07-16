from log import LogPrintMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado == False:
            self._ligado = True

    def desligar(self):
        if self._ligado == True:
            self._ligado = False

class Smartphone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f"{self._nome} Ligado!"
            self.log_sucess(msg)
    
    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg =  f"{self._nome} Desligado!"
            self.log_error(msg)

