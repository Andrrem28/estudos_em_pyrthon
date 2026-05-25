'''
Dicionários em Python (Tipo Dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".

Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple e etc...
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} - ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple.
Mutável: dict, list.

pessoa = {
	'nome' : 'Fco André',
	'sobrenome' : 'Martins',
	'idade' : 36,
	'altura' : 1.73,
	'enderecos' : [
		{
			'rua' : 'Tal',
			'numero' : '121',
			'bairro' : 'Bairro A',
			'cidade' : 'Mossoró'
		},

		{
			'rua' : 'Tal',
			'numero' : '121',
			'bairro' : 'Bairro B',
			'cidade' : 'Mossoró'
		},
	]
}


print(pessoa, type(pessoa))

'''
# pessoa = dict(nome="André", sobrenome="Martins") # Uma outra forma de criar um dicionário. 
pessoa = {
	'nome' : 'Fco André',
	'sobrenome' : 'Martins',
	'idade' : 36,
	'altura' : 1.73,
	'enderecos' : [
		{
			'rua' : 'Tal',
			'numero' : '121',
			'bairro' : 'Bairro A',
			'cidade' : 'Mossoró'
		},

		{
			'rua' : 'Tal',
			'numero' : '121',
			'bairro' : 'Bairro B',
			'cidade' : 'Mossoró'
		},
	]
}


# print(pessoa, type(pessoa))
print(pessoa['nome'])

for chave in pessoa:
	print(chave, pessoa[chave])