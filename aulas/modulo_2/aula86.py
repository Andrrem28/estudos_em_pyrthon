# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# lista = [
# 	n * 2 
# 	for n in range(10)
# ]

# print(lista)

import pprint

def output(lista):
	pprint.pprint(lista, sort_dicts=False, width=40)


# Mapeamento de dados em list comprehension
produtos = [
	{
		'nome' : 'Arroz', 'preco' : 10
	},
	{
		'nome' : 'Feijão', 'preco' : 15
	},
	{
		'nome' : 'Macarrão', 'preco' : 2
	},
]

# novos_produtos = [
# 	produto
# 	for produto in produtos
# ]

# novos_produtos = [
# 	produto['preco']
# 	for produto in produtos
# ]

# novos_produtos = [
# 	{
# 		'nome': produto['nome'],
# 		'preco' : produto['preco']
# 	}
# 	for produto in produtos
# ]

# novos_produtos = [
# 	{**produto, 'preco' : produto['preco'] * 1.05}
# 	for produto in produtos
# ]

# novos_produtos = [
# 	{**produto, 'preco' : produto['preco'] * 1.05}
# 	if produto['preco'] > 5 else {**produto}
# 	for produto in produtos
# ]

novos_produtos = [
	{**produto, 'preco' : produto['preco'] * 1.05}
	if produto['preco'] > 5 else {**produto}
	for produto in produtos
	if (produto['preco'] > 5 and produto['preco'] * 1.05) > 10
]

# print(*novos_produtos, sep='\n')


# Mapeamento de dados em list com filtro
lista = [n for n in range(10) if n < 5]

output(novos_produtos)