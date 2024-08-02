import os

caminho = os.path.join("C:\\Users", "Joao", "Videos", "Filmes")
count = 0

#Diretorio atual (root) - lista de subdiretorios (dirs) - arquivos do diretorio atual (files)
for root, dirs, files in os.walk(caminho):
    count += 1
    print(count, "Pasta atual", root)

    for diretorio in dirs:
        print("   ", count, "Dir:", diretorio)

    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)
        print("   " , count, "FILE:", caminho_completo_arquivo)