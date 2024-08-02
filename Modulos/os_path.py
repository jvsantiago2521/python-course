import os #interacao com o sistema operacional

#faz o sistema limpar o terminal
os.system("cls")

#cria um caminho
caminho = os.path.join("Desktop", "Novo", "caminho", "criado.txt")
print(caminho)

#separa o caminho do nome do arquivo em tuplas
print(os.path.split(caminho))
diretorio, arquivo_final = os.path.split(caminho)
print(diretorio)
print(arquivo_final)

#separa o nome do arquivo da extensao
nome_arquivo, extensao = os.path.splitext(arquivo_final)
print(nome_arquivo, extensao)


#verifica se umu caminho especifico existe no pc
print(os.path.exists("/Users/Joao/Documents/python-course"))

#verifica o item final desse diretorio
print(os.path.basename(caminho))

#encontra o caminho absoluto em que o programa esta
print(os.path.abspath(""))


#pega o caminho do diretorio sem contar com o arquivo
print(os.path.dirname(caminho))



