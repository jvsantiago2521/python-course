import json
import os

NOME_ARQUIVO = "json_arquivo2.json"
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(os.path.join(os.path.dirname(__file__), NOME_ARQUIVO))

json_string = {
    "name": "Joao Victor",
    "last_name": "Santiago Goncalves", 
    "is_man": True, 
    "height": 1.67, 
    "year_of_birth": 2004, 
    "characteristics": ["Lindo", "Cheiroso", "Forte"],
    "defect": None
}

#Criar arquivo json
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(json_string, arquivo, ensure_ascii=False, indent=2)

#Ler arquivo json
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    data_json = json.load(arquivo)
    print(data_json)
    print(data_json["name"])