'''
Função lambda em  Python
A função lambda é uma função como qualquer outra
em Python. Porém, são funções anônimas que contém
apenas uma lista, ou seja, tudo dever ser contido dentro de uma única
expressão
'''

lista = [
	{'nome' : 'André', 'sobrenome' : 'Martins'},
	{'nome' : 'Jacksielli', 'sobrenome' : 'Justino'},
	{'nome' : 'Marcos', 'sobrenome' : 'Freitas'},
	{'nome' : 'Bola', 'sobrenome' : 'Coquines'},
	{'nome' : 'Zebra', 'sobrenome' : 'Bolona'},
]

# lista = [4, 32, 1, 2, 5, 6, 3, 0]
# lista.sort(reverse=True)

def exibicao(lista):
	for item in lista:
		print(item)
	print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibicao(l1)
exibicao(l2)