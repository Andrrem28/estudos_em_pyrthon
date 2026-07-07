# O que é JSON - JavaScript Object Notation
# JSON - JavaScript Object Notation (extensão .json)
# É uma estrutura de dados que permite a serialização
# de objetos em texto simples para facilitar a transmissão de
# dados através da rede, APIs web ou outros meios de comunicação.
# O JSON suporta os seguintes tipos de dados:
# Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
# Strings: são cadeias de caracteres, como "Olá, mundo!" ou "12345"
#   As strings devem ser envolvidas por aspas duplas
# Booleanos: são os valores verdadeiro (true) ou falso (false)
# Arrays: são listas ordenadas de valores, como [1, 2, 3] ou
#   ["Oi", "Olá", "Bom dia"]
# Objetos: são conjuntos de pares chave/valor -> {"nome": "João", "idade": 30}
# null: é um valor especial que representa ausência de valor
#
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
from pprint import pprint
from typing import TypedDict


class Pessoa(TypedDict):
    nome: str
    idade: int
    cidade: str
    enderecos: list[dict[str, str | int]]

string_json = '''
            {
                "nome": "André",
                "idade": 36,
                "cidade": "Mossoró",
                "enderecos": 
                [
                        {
                            "rua": "Rua 1",
                            "numero": 123
                        }, 
                        {
                            "rua": "Rua 2",
                            "numero": 456
                        }
                    ]
            }'''

pessoa: Pessoa = json.loads(string_json)

# pprint(pessoa, width=30)

# pprint(pessoa['nome'])
# pprint(pessoa['idade'])
# pprint(pessoa['cidade'])
# pprint(pessoa['enderecos'][0])

print(json.dumps(pessoa, indent = 4, ensure_ascii = False))