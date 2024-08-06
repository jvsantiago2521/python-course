from pathlib import Path

caminho_projeto = Path()

#Retorna o caminho absoluto do projeto
print()
print(caminho_projeto.absolute())
print()

#Retorna o caminho desse arquivo path_lib.py
caminho_arquivo = Path(__file__)
print()
print(caminho_arquivo)
print()

#Retorna o caminho mae desse arquivo path_lib.py
print()
print(caminho_arquivo.parent)
print()

print()
ideais = caminho_arquivo.parent / "ideias" / "novo_caminho"
print(ideais)

arquivo = Path.home() / "Desktop" / "arquivo.txt"
#Cria o arquivo no caminho especificado
arquivo.touch()
#Escreve u texto dentro do arquivo ciado
arquivo.write_text("Ola mundo!")
#Le o conteudo do arquivo
print(arquivo.read_text())
#Apaga o arquivo criado 
arquivo.unlink()

caminho_teste = Path.home() / "Desktop" / "teste.txt"

with caminho_teste.open("a+") as file:
    file.write("Uma linha\n")
    file.write("Outra linha\n")

print(caminho_teste.read_text())
