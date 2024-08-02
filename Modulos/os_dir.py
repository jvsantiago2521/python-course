import os

caminho = r"C:\\Users\\Joao\\Videos\\Filmes"
caminho = os.path.join("C:\\Users", "Joao", "Videos", "Filmes")
print(caminho)
print(os.path.exists(caminho))

#lista os itens de um diretorio
for item in os.listdir(caminho):
    #cria um caminho com o final sendo os itens desse diretorio
    caminho_completo_pasta = os.path.join(caminho, item)
    #se o caminho criado nao for uma pasta, da um print no nome do arquivo
    if not os.path.isdir(caminho_completo_pasta):
        print(item)
    #se nao entra em um loop onde lista os arquiuvos dentro dessas pastas
    else:
        for item in os.listdir(caminho_completo_pasta):
            print(item)