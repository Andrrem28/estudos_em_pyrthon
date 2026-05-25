# Manipulando chaves e valores em dicionários.

pessoa = {}

chave = 'nome' # key (chave do dicionário)

pessoa[chave] = 'Fco André' # value (valor pra chave nome do dicionário)
 
pessoa['sobrenome'] = 'Martins' # value (valor pra chave sobrenome do dicionário)

print(pessoa[chave]) # Exibe o valor da chave nome no output

pessoa[chave] = 'Jacksielli' # new value (novo valor para a chave nome do dicionário)

print(pessoa[chave]) # Exibe o novo valor da chave nome no output

del pessoa['sobrenome'] # del (para poder deletar uma chave do dicionário)

print(pessoa) # Exibirá o dicionário pessoa, sem a key 'sobrenome'
print(pessoa['nome']) # Exibirá o valor da key (chave), nome do dicionário. Mostrando que mesmo deletando a chave 'sobrenome', podemos manilupar o valor da chave.

# O método get() verífica se existe a chave no dicionário.
# O valor padrão é None, mas também posso alterar o valor do segundo arumento. 
# Ex: pessoa.get('sobrenome', 'Valor padrão')

if pessoa.get('sobrenome', None) is None:
	print('A chave não existe')
else:
	print('A chave existe')