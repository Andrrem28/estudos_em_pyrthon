''' 
Exercício. Criando uma Calculadora com while
'''
while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite digite outro número: ')

    operador = input('Digite um operador (+, -, /, *): ')

    num_validos = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)

        num_validos = True
    except:
        num_validos = None


    if num_validos is None:
        print('Um ou ambos os valores digitados estão incorretos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando a sua conta. Confira o resultado abaixo.')
    if operador == '+':
        print(f'A soma de {n1_float} e {n2_float}, é igual a: ', n1_float + n2_float)
    elif operador == '-':
        print(f'A subtração de {n1_float} e {n2_float}, é igual a: ', n1_float - n2_float)
    elif operador == '/':
        print(f'A divisão de {n1_float} e {n2_float}, é igual a: ', n1_float / n2_float)
    elif operador == '*':
        print(f'A multiplicação de {n1_float} e {n2_float}, é igual a: ',n1_float * n2_float)
    else:
        print('Deu algo de errado...')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
