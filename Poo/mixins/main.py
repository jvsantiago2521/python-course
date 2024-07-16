import os
from eletronico import Smartphone
os.system("cls")

galaxy_s = Smartphone("Galaxy S")
iphone = Smartphone('Iphone')

galaxy_s.ligar()
galaxy_s.desligar()
iphone.ligar()
iphone.desligar()

print()