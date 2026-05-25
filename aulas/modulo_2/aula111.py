# map - para mapear dados
from functools import partial

def print_iter(iterator):
	print(*list(iterator), sep = '\n')
	print()


produtos = [
	{'nome': 'Produto 5', 'preco': 11.11},
	{'nome': 'Produto 2', 'preco': 42.12},
	{'nome': 'Produto 1', 'preco': 41.10},
	{'nome': 'Produto 3', 'preco': 55.50},
	{'nome': 'Produto 6', 'preco': 22.90},
	{'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
	return round(valor * porcentagem, 2)

aumenta_dez_porcento = partial(
		aumentar_porcentagem,
		porcentagem = 1.1
	)

def altera_valor_produto(produto):
	return {
		**produto,
		'preco': aumenta_dez_porcento(
			produto['preco']
		)}

# novos_produtos = [
# 	{**p, 'preco': aumenta_dez_porcento(p['preco'])} for p in produtos
# ]

novos_produtos = list(map(
		altera_valor_produto,
		produtos
	))

print(produtos)
print(novos_produtos)

print(list(map(lambda x: x * 3, [2, 4, 6])))