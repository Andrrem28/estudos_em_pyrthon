'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append -> Adiciona um item no final,
    insert -> Adiciona um item no índice escolhido,
    pop -> Remove do final ou do índice escoolhido,
    del -> Apaga um índice,
    clear -> Limpa lista, 
    extend -> Estende a lista,
    + -> Concatena as listas.

Create, Read, Update, Delete
criar, ler, atualizar, apagar = lista[i] (CRUD)
'''
# lista = [10, 20, 30, 40]   

# # del lista[2] # irá remover o conteúdo atual do indíce 2
# # print(lista[2])

# lista.append(50) # Adiciona um novo valor no final da lista, criando um novo indíce.

# lista.pop() # Remove o conteúdo do último índice. Você pode colocar também .pop(i) para remover um conteúdo específico do indíce

# lista.append(60) # Adiciona um novo valor no final da lista, criando um novo indíce.

# lista.insert(0, 40)

# print(lista) 

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b # Junta os valores da lista_a com a lista_b
lista_a.extend(lista_b) # Junta os valores da lista_a com a lista_b
print(lista_c)