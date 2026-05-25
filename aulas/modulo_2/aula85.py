# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

# lista = []

# for n in range(10):
# 	lista.append(n)

# print(lista)

lista = [
	n * 2 
	for n in range(10)
]

print(lista)

