numeros = 1, 2, 3, 4

#Permite colocar quantidade infinita de argumentos não nomeados no parametro
#Empacota todos os argumentos dentro de uma tupla
def soma(*args):
    resultado = 0
    for num in list(args):
        resultado += num
    print(resultado)

numeros = 1, 2, 3, 4

#soma(1, 2, 3, 4)
#soma(*numeros)

##################################################################

pessoa = {
    "nome": "joao",
    "sobrenome": "santiago"
}

dados_pessoa = {
    "altura": 1.70,
    "idade": 20
}

pessoa_completa = {**pessoa, **dados_pessoa, "sexo": "masculino"}
print(pessoa_completa)