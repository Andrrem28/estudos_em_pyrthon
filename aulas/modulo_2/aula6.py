'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento de tuplas)
'''

# Revisão sobre desempacotamento de tuplas
# x, y, *rest = 1, 2, 3, 4, 5

# print(f"x: {x}, y: {y}, rest: {rest}")

# def soma(x, y):
#     return x + y

def soma_valores(*args):
    total = 0
    
    for numero in args:
        print('Total', total, 'Número', numero)
        total += numero
        
    return print('Total final:', total)

soma_valores(1, 2, 3, 4, 5)  # A função soma_valores pode receber um número variável de argumentos

def loop(*args):
    for arg in args:
        print(arg)

loop(1, 2, 3, 4, 5)  # A função loop pode receber um número variável de argumentos

def soma(*args):
    return print(sum(args))

soma(1, 2, 3, 4, 5)  # A função soma pode receber um número variável de argumentos

