# Exercício - Salve sua classe em JSON
# Salve dos dados da sua classe em JSON e depois crie novamente as instâncias
# da classe com os dados salvos.
# Faça em arquivos separados.

CAMINHO_ARQUIVO = 'banco_de_dados.json'

import json

class Pessoa: 
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

p1 = Pessoa('André', 36)
p2 = Pessoa('Jacksielli', 31)
p3 = Pessoa('Marcos', 7)

db = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
	with open(CAMINHO_ARQUIVO, 'w') as arquivo:
		json.dump(db, arquivo, ensure_ascii= False, indent = 2)