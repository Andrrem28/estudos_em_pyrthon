# Explicando a ordem dos Decoradores

def parametros_decorador(nome):
	def decorador(func):
		print('Decorador: ', nome)
		def sua_nova_funcao(*args, **kwargs):
			res = func(*args, **kwargs)
			valor_final = f'{res} {nome}'
			return valor_final
		return sua_nova_funcao
	return decorador

@parametros_decorador(nome = '4')
@parametros_decorador(nome = '3')
@parametros_decorador(nome = '2')
@parametros_decorador(nome = '1')
def soma(x, y):
	return x + y

soma_numeros = soma(20, 30)

print(soma_numeros)