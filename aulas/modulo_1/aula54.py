'''
enumerate -> enumera iteráveis (índices)
'''

lista = ['André', 'Jacksielli', 'Marcos']

lista.append('Theo')

# lista_enumerada = list(enumerate(lista)) # type coersion para tupla, para criar um índice.

# print(next(lista_enumerada))

# for item in enumerate(lista): # type coersion para tupla, para criar um índice.
#     indice, nome = item
#     print(indice, nome)
#     print(item)

for indice, nome in enumerate(lista): # type coersion para tupla, para criar um índice.
    print(f'{indice}, {nome}, Valor pego do índice -> {lista[indice]}')

# for tupla_enumerada in enumerate(lista): # type coersion para tupla, para criar um índice.
#     print('For da Tupla')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
