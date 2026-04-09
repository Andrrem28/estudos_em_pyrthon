'''
split e join com list e str
split -> divide uma string
join -> une uma string
'''

frase = 'Barquinho on Python'

lista_palavras = frase.split() # Parametro default é o ' ' (espaço)

lista_palavras_empty = []

for i, palavra in enumerate(lista_palavras):
    lista_palavras_empty.append(lista_palavras[i].strip())
    # lista_palavras[i] = lista_palavras[i].strip()
    # print(lista_palavras[i].strip())
    # print(lista_palavras[i].lstrip())
    # print(lista_palavras[i].rstrip())

frase_join = ''.join(lista_palavras_empty) 

print('Sem o join')
print(lista_palavras_empty)
print('Sem com join')
print(frase_join)