import json
from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    name: str
    last_name: str
    is_man: bool
    height: float
    year_of_birth: int
    characteristics: list[str]
    defect: None | float

string_json = '''
{
    "name": "Joao Victor",
    "last_name": "Santiago Goncalves", 
    "is_man": true, 
    "height": 1.67, 
    "year_of_birth": 2004, 
    "characteristics": ["Lindo", "Cheiroso", "Forte"],
    "defect": null
}
'''

#Carrega um json usando o conteudo da variavel
filme: Movie = json.loads(string_json)

#Formata a string json, tratando erros ascci
json_string = json.dumps(filme, ensure_ascii=False, indent=2)

print(filme)
print(json_string)
print(filme['name'])