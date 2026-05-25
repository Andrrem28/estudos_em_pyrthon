# Exercício - Adiando execução de funções
def soma(x, y):
	return x + y

def multiplica(x, y):
	return x * y

def criar_funcao(funcao, x):
	def funcao_interna(y):
		return funcao(x, y)
	return funcao_interna

soma = criar_funcao(soma, 5)
multiplica = criar_funcao(multiplica, 10)

print(soma(10))
print(multiplica(5))