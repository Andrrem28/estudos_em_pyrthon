'''
Cuidados com dados mutáveis
= -> Copiado o valor (imutáveis)
= -> Aponta para o mesmo valor na memória (mutável)
'''

nome = 'André'
var = nome
nome = 'Martins'

print(var, nome)

lista_a = ['André', 'Martins', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Texto'
print(lista_a)
print(lista_b)