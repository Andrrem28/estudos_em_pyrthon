'''
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''

# txt = iter('André') # __iter__()

# print(next(txt)) # __next__()

# Abaixo é um exemplo simples, de como funciona um laço de for por debaixo dos panos.
# txt = 'André' # iterável

# iterador = iter(txt) # iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

txt = 'André'

for l in txt:
    print(l)