from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f"E-mail: enviando - {self.mensagem}")
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f"SMS: enviando - {self.mensagem}")
        return True

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print("Notificação enviada!")
    else:
        print("Notificação NÃO enviada!")


sms = NotificacaoSMS("Oi")
notificar(sms)
email = NotificacaoEmail("Tchau")
notificar(email)


