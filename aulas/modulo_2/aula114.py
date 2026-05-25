# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# úteis para dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que não a recursão
# - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

# def fn_recursiva(inicio = 0, fim = 10):
#  	# Caso base
#  	if inicio >= fim:
#  		return fim

#  	'''
#  		Caso recursivo
#  		contar até chegar ao final 
#  	'''
#  	inicio += 1
#  	return fn_recursiva(inicio, fim)


# print(fn_recursiva())

def factorial(n):
	if n <= 1:
		return 1

	return n * factorial(n - 1)


print(factorial(5))
print(factorial(2))