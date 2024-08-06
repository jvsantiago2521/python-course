import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "csv_file.csv"

lista_clientes = [
    {"Nome": "Gabriel", "Sobrenome": "Lucas", "Idade": 16}, 
    {"Nome": "Laura", "Sobrenome": "Lima", "Idade": 20}, 
    {"Nome": "Claudio", "Sobrenome": "Brasil", "Idade": 38}
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo)

    escritor.writerow(nome_colunas)

    for cliente in lista_clientes:
        escritor.writerow(cliente.values())