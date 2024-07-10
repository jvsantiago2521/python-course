class Foo:
    def __init__(self):
        self.public = "isso é publico"
        self._protected = "isso é protegido"
        self.__private = "isso é privado"
    
    def public_m(self):
        return "metodo publico"
    
    def _protected_m(self):
        return "metodo protegido"
    
    def __private_m(self):
        return "metodo privado"
    
    def mostra_private(self):
        print(self.__private)
        print(self.__private_m())
    
f = Foo()
print(f.public)
print(f.public_m())
print(f._protected)
print(f._protected_m())
f.mostra_private()
