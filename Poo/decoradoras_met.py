def my_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f"{class_name}({class_dict})"
    return class_repr 

def add_repr(cls):
    cls.__repr__ = my_repr
    return cls

def my_planet(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        
        if "Terra" in resultado:
            return "Voce esta em casa"

        
        return resultado
    return interno

@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @my_planet
    def speak_name(self):
        return f"O nome do planeta é {self.nome}"

flamengo = Time("Flamengo")
vasco = Time("Vasco")
terra = Planeta("Terra")
marte = Planeta("Marte")

print(flamengo)
print(vasco)
print(terra)
print(marte)

print(terra.speak_name())
print(marte.speak_name())