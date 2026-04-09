'''
Exercício
Exiba os índices da lista
0 'Arroz'
1 'Feijão'
2 'Macarrão'
'''

lista = ['Arroz', 'Feijão', 'Macarrão']
indices = range(len(lista)) # Cria o tamanho da lista de acordo com a quantidade de valores no array

for i in indices:
    print(i, lista[i])