import random

#random.randrange(inicio do range, fim do range, quantos numeros vao ser pulados)
r_range = random.randrange(10, 20, 2)

#Vai printar um numero aleatorio dentro de (10, 12, 14, 16, 18)
print(r_range)

#Nao possui o parametro de numeros para pular
r_int = random.randint(10, 20) 

print(r_int)

#Retorna um valor com o mesmo intervalo, porem de ponto flutuante
r_uniform= random.uniform(10, 20) 

print(r_uniform)

nomes = ["João", "Luiz", "Renata", "Maria"]
#Embaralha a lista ORIGINAL
random.shuffle(nomes)
print(nomes)

#Cria uma nova lista com 2 nomes aleatorios da lista original (NAO REPETE VALORES)
novos_nomes = random.sample(nomes, k=2)
print(novos_nomes)

#Cria uma nova lista com 2 nomes aleatorios da lista original (REPETE VALORES)
novos_nomes2 = random.choices(nomes, k=2)
print(novos_nomes2)

#Pega apenas UM nomes da lista
nome_aleatorio = random.choice(nomes)
print(nome_aleatorio)

