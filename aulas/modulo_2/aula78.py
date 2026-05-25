# Métodos úteis dos dicionários em Python
# Criando um dicionário.
pessoa = {
	'nome' : 'André',
	'sobrenome' : 'Martins',
}

# len - Quantas chaves
print(len(pessoa))

# keys - Iterável com as chaves
print(pessoa.keys())
print(list(pessoa.keys())) # Usando coerção no dicionário.

# values - Iterável com os valores
print(pessoa.values())

# items - Iterável com as chaves e valores
print(pessoa.items())

for chave, valor in pessoa.items():
	print(chave, valor)

# setdefault - Adiciona valor se a chave não existe
pessoa.setdefault('idade', None)
print(pessoa['idade'])

# copy - Retorna uma cópia rasa (shallow copy)

#import copy 

'''
 Obs sobre o copy: Caso use apenas o método copy, caso o dicionário tenha sub-níveis (listas como um valor da chave por exemplo),
 o método copy usado via chamada de objeto, ele não irá copiar todo o conteúdo do dicionário, mas sim, irá fazer apenas uma cópia rasa (o shallow copy)
 para poder copiar todo o conteúdo, do dicionário para uma outra variável, importar a biblioteca copy (import copy), e usar o método chamado deepcopy (cópia profunda)
 para poder copiar todo o conteúdo de um dicionário, para uma variável, criando outro dicionário, sem afetar os valores do dicionário original.
'''
d1 = {
	'c1' : 1,
	'c2' : 2,
	'l1' : [0, 2, 4],
}

d2 = d1.copy()
#d2 = copy.deepcopy(d1)

d2['c1'] = 100
d2['l1'][1] = 444 # Usando está forma, irá afetar o valor dos dois dicionários, pois alocam o mesmo espaço na memória.

print(d1)
print(d2)

# get - Obtém uma chave
carro = {
	'cor' : 'Azul',
	'qtd_portas' : 4,
}

print(carro.get('cor', 'Não Existe')) # O valor padrão é None, então não precisa declarar após o nome da chave (key), mas caso declare, irá aparecer o valor informado, caso não exista a chave.

# pop - Apaga um item com a chave especificada (del)

cor = carro.pop('cor')

print(carro)
# popitem - Apaga o último item adicionado
moto = {
	'cor' : 'Preta',
	'tipo_cambio' : 'Automática'
}

ult_chave = moto.popitem()

print(moto)
# update - Atualiza um dicionário com outro

# moto.update({
# 		'tipo_ignicao' : 'Partida',
# 		'ano_modelo' : 2026
# 	})

# moto.update(tipo_ignicao='Partida', ano_modelo=2026) # Usando argumentos nomeados

# tupla = ('tipo_ignicao', 'Partida'), ('ano_modelo', 2026) # Exemplo com tuplas.

lista = [['tipo_ignicao', 'Partida'], ['ano_modelo', 2026]] # Exemplo com listas.

moto.update(lista)

print(moto)



