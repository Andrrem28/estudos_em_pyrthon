'''
Lista de listas e seus indices
'''

salas = [
    ['Marcos', 'Paulo'],
    ['André'],
    ['Jacksielli', 'André', 'Marcos']
    # ['Jacksielli', 'André', 'Marcos', (0, 1, 2, 3, 4)]
]

# print(salas[2][3][2]) # Pegando o valor de forma direta.

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(f'O aluno é {aluno}')

# print(salas)