import os
import shutil

#Pega o caminho da minha HOME
HOME = os.path.expanduser("~")
PYTHON_COURSE = os.path.join(HOME, "Documents\\python-course\\Modulos\\pasta_para_testes")
PASTA_ORIGINAL = os.path.join(PYTHON_COURSE, "pasta1")
NOVA_PASTA = os.path.join(PYTHON_COURSE, "copia_pasta1")
PASTA_PARA_MOVER = os.path.join(HOME, "Documents\\python-course\\Modulos")

#Apago uma pasta
shutil.rmtree(NOVA_PASTA, ignore_errors=True)

#Copio o conteudo de uma pasta e mando para outro diretorio (Nao pode existir, pois aqui que sera criado)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

#Renomeia/Move uma pasta
shutil.move(NOVA_PASTA, NOVA_PASTA + "_MOVED")

shutil.move(PASTA_ORIGINAL, PASTA_PARA_MOVER)