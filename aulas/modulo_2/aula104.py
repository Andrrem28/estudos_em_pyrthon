# Decoradores (Decorators) com parâmetros.

def fabrica_decoradores(a = None, b = None, c = None):
	def fabrica_funcoes(func):
		print('Decorador 1')
		def aninhada(*args, **kwargs):
			print('Parâmetros do decorador', a, b, c)
			print('Aninhada')
			res = func(*args, **kwargs)
			return res
		return aninhada
	return fabrica_funcoes	

@fabrica_decoradores(2, 4, 6)
def soma(x, y):
	return x + y

decoradoras = fabrica_decoradores(2, 4, 5)(lambda x, y: x * y)

soma_numeros = soma(10, 5)

multiplica_numeros = decoradoras(5, 10)

print(multiplica_numeros)
print(soma_numeros)