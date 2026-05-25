# reduce - faz a recução de um iteravel em um valor

from functools import reduce

produtos = [ 
	{'nome': 'Produto 3', 'preco': 9.22},
	{'nome': 'Produto 2', 'preco': 11.41},
	{'nome': 'Produto 1', 'preco': 52.45},
	{'nome': 'Produto 4', 'preco': 4.21},
	{'nome': 'Produto 5', 'preco': 10.22},
]

# def funcao_reduce(acumulador, produto):
# 	print('acumulador', acumulador)
# 	print('produto', produto)
# 	print()
# 	return acumulador + produto['preco']

# total = reduce(
# 	funcao_reduce,
# 	produtos,
# 	0
# )

total = reduce(
	lambda ac, produto: ac + produto['preco'],
	produtos,
	0
)

print('Total', total)

# total = 0
# for produto in produtos:
# 	total += produto['preco']
# print(total)

# print(sum([produto['preco'] for produto in produtos]))