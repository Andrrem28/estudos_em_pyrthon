# Exercício - Unir listas
# Criar uma função chamada zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menos lista.
# Ex: 
# ['Fortaleza', 'Natal', 'Salvador']
# ['CE', 'RN', 'AC', 'BH']
# Resultado
# [ ('Fortaleza', 'CE'), ('Natal', 'RN'), ('Rio Branco', 'AC'), ('Salvador', 'BH')]


# def zipper(lista1, lista2):
# 	intervalo = min(len(lista1), len(lista2))

# 	return [(lista1[i], lista2[i]) for i in range(intervalo)]

from itertools import zip_longest

lista1 = ['Fortaleza', 'Natal', 'Salvador']
lista2 = ['CE', 'RN', 'AC', 'BH']

print(list(zip_longest(lista1, lista2, fillvalue="Sem Cidade")))