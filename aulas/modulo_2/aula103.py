# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradoras de outras funções
# Decoradores são "Syntax Sugar" (Açúcar Sintático)

def criar_funcao(func):
	def funcao_interna(*args, **kwargs):
		print('Decorando função')
		for arg in args:
			e_string(arg)
		resultado = func(*args, **kwargs)
		print('Ok! A função foi decorada')
		return resultado
	return funcao_interna

def e_string(param):
	if not isinstance(param, str):
		raise TypeError(f'{param} deve ser uma string')

# checa_invercao_da_string = criar_funcao(inverte_string)

@criar_funcao
def inverte_string(string):
	print(f'{inverte_string.__name__}')
	return string[::-1]

string_inversa = inverte_string('123')

print(string_inversa)