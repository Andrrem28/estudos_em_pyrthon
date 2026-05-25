# Empacotamento e desempacotadmento de dicionário

# a, b = 1, 2
# a, b = b, a

# print(a, b)

# a, b = pessoa.values()
# a, b = pessoa.items()
# (a1, a2), (b1,b2) = pessoa.items()

# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
# 	print(chave, valor)

pessoa = {
	'nome' : 'André',
	'sobrenome' : 'Martins'
}

dados_pessoa = {
	'idade' : 36,
	'altura' : 1.73
}

pessoa_completa = {**pessoa, **dados_pessoa, 'cor_olhos': 'Verde Claro'}

# print(pessoa_completa)

# args e kwargs
# args (já vi)
# kwargs - keyword arguments (argumentos nomeados)

def exibi_argumentos_nomeados(*args, **kwargs):
	print('Argumentos não nomeados', args)


	for chave, valor in kwargs.items():
		print(chave, valor)

# exibi_argumentos_nomeados('Marcos', nome='André')
exibi_argumentos_nomeados(**pessoa_completa)