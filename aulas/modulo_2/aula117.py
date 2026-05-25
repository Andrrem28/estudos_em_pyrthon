# Aula sobre o formato módulo JSON

import json

# pessoa = {
# 	'nome': 'Francisco André',
# 	'sobrenome': 'Martins',
# 	'idade': 36,
# 	'enderecos': [
# 		{'rua': 'Rua 1', 'numero': 123},
# 		{'rua': 'Rua 2', 'numero': 321},
# 	],

# 	'altura': 1.67,
# 	'peso': 90,
# 	'numero_preferidos': (14, 22, 50, 100),
# 	'dev' : True,
# 	'nada': None,
# }

# with open('aula117.json', 'w', encoding = 'utf8') as arquivo:
# 	json.dump(
# 		pessoa,
# 		arquivo,
# 		ensure_ascii = False, # O ensure_ascii parâmetro, sendo igual a False, ele vai manter as acentuações dos valores 
# 		indent = 2,
# 	) 

with open('aula117.json', 'r', encoding='utf8') as arquivo:
	pessoa = json.load(arquivo)
	# print(pessoa)
	# print(type(pessoa))
	print(pessoa['nome'])