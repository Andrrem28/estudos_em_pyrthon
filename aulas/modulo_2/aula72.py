# Aula A

# Exercícios com funções

# Crie uma função que multiplica todos os argumentos (parametros)
# não nomeados recebidos.

# Retorne o total para uma variável e mostre o valor da variável.

def multiplicar(*args):
	total = 1
	for numero in args:
		total *= numero

		print(numero)

	return total

resultado_multiplicacao = multiplicar(2, 4, 6, 8, 10)

# Crie uma função que fala se o número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_ou_impar(numero):
	multiplo_de_dois = numero % 2 ==0

	if multiplo_de_dois:
		return print(f'O número {numero} é par')
	
	return print(f'O número {numero} é ímpar')


par_ou_impar(2)
par_ou_impar(3)