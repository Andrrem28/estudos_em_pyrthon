'''
Operadores lógicos
and (e), or (ou) e not (não)
and - Todas as condições precisam ser verdadeiras
Se qualquer valor for considerado falso, 
a expressão inteira será alaiada naquele valor
são considerados falsy
0 0.0 '' False
Também existe um tipo chamado de None que é
usado para representar um não valor.
'''
entrada = input('[E]entrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'
# Uso do operador or
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito. Ex:
print(True and False and True) # Resultado será True
print(True and 0 and True) # Resultado será True