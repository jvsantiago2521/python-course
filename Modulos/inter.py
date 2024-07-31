import calendar
import locale

#Mudando todas as categorias, para a localidade do sistema operacional -> ''
locale.setlocale(locale.LC_ALL, '')

#Mudando todas as categorias, para a localidade pt_BR
locale.setlocale(locale.LC_ALL, 'pt_BR')

print(calendar.calendar(2022))