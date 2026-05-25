'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x, y, z):
    # Definição
    print(f'O valor de {x=}, {y=} e {z=} somados dão', '|', x + y + z)

# Argumento não nomeado + execução de função
soma(3, 3, 3)
# Obs: Quando for nomeado algum argumento. Do declarado em diante, devem ser todos nomeados.
# Ex:
#    soma(4, y=3, 5) <- Desta forma irá causar erro, pois o y foi nomeado.
#    soma(3, y=3, z=5) <- Desta forma não irá causar erros, pois esta nomeado de forma correta.
# Argumento nomeado
soma(y=3, x=4, z=6)