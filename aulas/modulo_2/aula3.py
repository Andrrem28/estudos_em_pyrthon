'''
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter
valores padrão. Caso o valor não seja enviado
para o parâmetro, o valor padrão será usado.
'''

def soma(x, y, z = None):
    if z is None:
        print(f'O valor de {x=} e {y=} somados dão', '|', x + y)
    else:
        print(f'O valor de {x=} e {y=} e {z=} somados dão', '|', x + y + z)

# def soma(x, z = None, y): # <- Desta forma irá causar erro, pois o parâmetro y não tem valor padrão e está depois do z que tem valor padrão.
#     if z is None:
#         print(f'O valor de {x=} e {y=} somados dão', '|', x + y)
#     else:
#         print(f'O valor de {x=} e {y=} e {z=} somados dão', '|', x + y + z)

soma(9, 15)

soma(10, 50, 15)

soma(y=5, x=9, z=18)