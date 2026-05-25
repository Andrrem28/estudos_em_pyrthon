# dir, hasattr, getattr, setattr em Python

string = 'André'
metodo = 'upper'
if hasattr(string, 'upper'):
	print('Existe a função upper')
	print(getattr(string, metodo)())
	print(string.upper())
else:
	print('Método não existente.')