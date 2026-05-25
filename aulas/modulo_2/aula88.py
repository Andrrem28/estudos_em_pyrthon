# Dictionary Comprehension e Set Comprehension
produto = {
	'nome' : 'Arroz',
	'preco' : 2.50,
	'categoria' : 'Alimento'
}

new_dc = {
	chave: valor.upper()
	if isinstance(valor, str) else valor
	for chave, valor in produto.items()
	if chave == 'categoria'
}

lista = [
	('a', 'valor a'),
	('b', 'valor b'),
	('c', 'valor c'),
]

other_dc = {
	chave: valor
	for chave, valor in lista
}

# print(other_dc)


set_1 = {i for i in range(10)}

print(set_1)