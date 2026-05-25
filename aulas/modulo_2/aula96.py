# raise - lançando exceções (erros)

def valor_nao_divisivel(d):
	if d == 0:
		raise ZeroDivisionError('Este valor não pode ser divisível.')
	return True

def verifica_tipo_numero(n):
	tipo_n = type(n)

	if not isinstance(n, (int, float)):
		raise TypeError(
			f'{n} informar apenas número inteiros ou de ponto flutuante'
			f'{tipo_n.__name__} enviado.'
		)
	return True

def divide(n, d):
	verifica_tipo_numero(n)
	verifica_tipo_numero(d)
	valor_nao_divisivel(d)

	return n / d

divide(8, 0)