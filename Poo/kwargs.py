#Permite colocar quantidade infinita de argumentos NOMEADOS no parametro
def mostra_argumentos(**kwargs):
    print(kwargs)

mostra_argumentos(nome="joao", sobrenome="santiago")