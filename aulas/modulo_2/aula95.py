# Try, except, else finally

# try:
# 	a = 19
# 	b = 0
# 	print('Linha antes da divisão')
# 	print('Forçando error de index'[100])
# 	c = a / b
# 	print('Linha depois da divisão')
# except ZeroDivisionError:
# 	print('Não  é possível dividir por 0.')
# except NameError:
# 	print('Nome da variável não reconhecido.')
# except (TypeError, IndexError) as error: # as (alias) você declara um nome personalizado para as classes de error para tratar o mesmo.
# 	print('Tipo de valor não aceito ou Index não existente.')
# 	print('MSG: ', error)
# 	print('Nome: ', error.__class__.__name__)
# except Exception:
# 	print('Error desconhecido.')
# 	

try:
	print('Linha antes da divisão.')
	8 / 0
	print('Linha depois da divisão')
except ZeroDivisionError:
	print('Error')
else:
	...
finally: # O finally sempre será executado.
	print(321)