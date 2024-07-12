class A:
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print("A")

class B(A):
    def __init__(self, atributo, outro):
        super().__init__(atributo)
        self.outro = outro

    def metodo(self):
        print("B")

class C(B):
    def metodo(self):
        super(B, self).metodo() #A
        super(C, self).metodo() #B
        print("C") #C

test = C("Atributo", "Outro")
print(test.atributo, test.outro)
test.metodo()