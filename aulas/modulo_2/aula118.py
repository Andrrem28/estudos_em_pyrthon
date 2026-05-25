# Problema dos parâmetros mutáveis em funções Python

def adiciona_cliente(nome, lista = None):
	if lista is None:
		lista = []

	lista.append(nome)
	return lista


cliente_1 = adiciona_cliente('André')

cliente_2 = adiciona_cliente('Marcos')

print(cliente_1)
print(cliente_2)