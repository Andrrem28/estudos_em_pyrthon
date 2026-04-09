'''
Operador lódigo "not"
Usado para inverter expressões
not True = False
not False = True
'''

# Exemplo apenas para exibir a mensagem de texto para o usuário
# quando ele não digitar nenhum valor de entrada.
senha = input('Senha: ')

if not senha:
    print('Você digitou nada')

print(not True) # False
print(not False) # True