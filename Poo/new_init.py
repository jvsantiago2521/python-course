#__new__ é o metodo responsavel por criar e retornar o novo objeto
#__init__ é o metodo responsavel por inicializar a instancia

class A:
    def __new__(cls):
        print("Antes de criar a instancia")
        instancia = super().__new__(cls)
        print("Depois de criar a instancia")
        return instancia 
    
    def __init__(self):
        print("Sou init")

    def __repr__(self):
        return f"{self.__class__.__name__}()"
    
a = repr(A())
print(a)