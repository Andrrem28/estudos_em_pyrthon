'''
Retorno de valores das funções (return)
'''

def soma(x, y):
    if x > 10:
        return "x é maior que 10"  # A função retorna uma string se x for maior que 10
    return x + y  # A função retorna a soma de a e y

resultado = soma(11, 5)  # A variável resultado recebe o valor retornado pela função soma
print(f"O resultado da soma é: {resultado}")

# var = print('Olá, mundo!')
# print(var) <- Isso não vai imprimir nada, pois a função print() retorna None