'''
Introdução ao tra/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

num_str = input(
    'Digite um número e eu lhe direi o dobro: '
    )

try:
    # print apenas para verificar o tipo antes da conversão
    print('STR: ', num_str)
    num_float = float(num_str)
    # print apenas para verificar o tipo depois da conversão
    print('FLOAT: ', num_float)
    print(f'O dobro do {num_str} é {num_float * 2:.2f}')    
except:
    print('Isso não é um número')