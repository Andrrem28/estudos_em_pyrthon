'''
Escopo de funções em Python
Escopo significa a região onde uma variável é reconhecida.
Em Python, existem dois tipos de escopo: local e global.
O escopo local é o escopo dentro de uma função, onde as variáveis são reconhecidas apenas dentro dessa função.
O escopo global é o escopo fora de todas as funções, onde as variáveis são reconhecidas em todo o programa.
Em Python, as variáveis definidas dentro de uma função são locais por padrão,
e as variáveis definidas fora de todas as funções são globais por padrão.
No entanto, é possível acessar variáveis globais dentro de uma função, mas para modificar uma variável global dentro de uma função
'''

def minha_funcao():
    x = 10  # Variável local
    print(f"Valor de x dentro da função: {x}")

def minha_funcao_global():
    global y  # Declarando que queremos usar a variável global y
    y = 20  # Modificando a variável global
    print(f"Valor de y dentro da função: {y}")

# Variável global
y = 5
print(f"Valor de y antes de chamar a função: {y}")
minha_funcao_global()
print(f"Valor de y depois de chamar a função: {y}")
