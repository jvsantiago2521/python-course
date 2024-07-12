class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...
    
cliente_ricardo = Cliente("Ricardo", "Vieira")
cliente_ricardo.falar_nome_classe()

aluno_joao = Aluno("Joao", "Victor")
aluno_joao.falar_nome_classe()

pessoa_sarah = Pessoa("Sarah", "Maria")
pessoa_sarah.falar_nome_classe()
