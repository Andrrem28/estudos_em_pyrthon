# Funções lambda mais complexas.

def executa(funcao, *args):
	return funcao(*args)

# def soma(x, y):
# 	return x + y

# def cria_multiplicador(multiplicador):
# 	def multiplica(numero):
# 		return numero * multiplicador
# 	return multiplica

# print(
# 	executa(
# 		lambda x, y: x + y,
# 		5, 10
# 	),
# 	executa(soma, 5, 10)
# )

duplica = executa(
	lambda m: lambda n: n * m,
	2 # Multiplicador 
)

print(duplica(4))


print(
	executa(
		lambda *args: sum(args),
		1, 4, 2, 6, 9, 10
	)
)