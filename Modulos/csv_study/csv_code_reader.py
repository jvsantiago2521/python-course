import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "csv_file.csv"

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha["Nome"])
        print(linha["Sobrenome"])
        print(linha["Idade"])