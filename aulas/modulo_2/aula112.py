# filter é um filtro funcional 

def print_iter(iterator):
	print(*list(iterator), sep = '\n')

produtos = [ 
	{'nome': 'Produto 3', 'preco': 9.22},
	{'nome': 'Produto 2', 'preco': 11.41},
	{'nome': 'Produto 1', 'preco': 52.45},
	{'nome': 'Produto 4', 'preco': 4.21},
	{'nome': 'Produto 5', 'preco': 10.22},
]

novos_produtos = filter(
	lambda p: p['preco'] > 10, produtos
)

print_iter(novos_produtos)

# novos_produtos = [ 
# 	p for p in produtos
# 	if p['preco'] > 10
# ]

# print_iter(produtos)