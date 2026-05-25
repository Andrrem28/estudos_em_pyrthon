# Sets - Conjuntos em Python (tipo set)
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3} 

# s1 = set() # Vazio  
# s1 = {'André', 1, 2, 3} # Com dados # Desta forma também é considerado um set, porém com os valores ordenados.

# print(s1) # Exibirá o iterável criado pelo set() e ele não vem de apresenta de forma ordenada.

# Sets são eficientes para remover alguns valores duplicados de iteráveis
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 4, 4, 4]
#  # s2 = {1, 2, 2, 2, 3, [1, 2]} # Desta forma o set não irá funcionar, pois não aceita valores mutáveis
# # s2 = {1, 2, 2, 2, 3, (12)} # Desta forma irá funcionar, com tupla.
# s2 = {1, 2, 2, 2, 3}

# # s2 = set(l1)
# l2 = list(s2)

# for numero in s2:
# 	print(numero)

# print(s2)
# print(l2)

# Métodos úteis:
# add, update, clear, discard
# Obs: A função add, para adicionar um novo valor em um set
# só aceita um valor por vez, caso queira por mais, sempre 
# deverá chamar a função add()

# s1 = set()
# s1.add('André')
# s1.add('Martins')

# s1.update(('Freitas',)) # Quando se usa o update, ele adiciona um novo valor ao set, porém de forma não ordenada.
# # Obs: Para poder mandar o valor, de forma completa e ordenada, use uma tupla.

# # s1.clear() # a função clear, limpa todo o set.
# s1.discard('André') # Para o discard, você precisa informar um valor no argumento.
# print(s1)


# Operações úteis:
# união | união (union) - Une
# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = s1 | s2

# intersecção & (intersection) - Itens presentes em ambos
# s3 = s1 & s2

# diferença - Itens presentes apenas no set da esquerda
# s3 = s1 - s2

# diferença simétrica ^ - Itens que não estão em ambos.
# s3 = s1 ^ s2

# print(s3)

# Exemplo de uso de sets.

letras = set()
while True:
	letra = input('Digite: ')
	letras.add(letra.lower())

	if 'a' in letras:
		print('Acertou')
		break

	print(letras)