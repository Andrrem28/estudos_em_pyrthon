'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira.
Loop infinito -> Quando um código não tem fim.
Obs.: Criar uma variável que irá ser o contador do seu laço, para que não se torne um laço infinito de repetição.
'''
# condicao = True

# while condicao:
#     nome = input('Qual o seu nome: ')
#     print(f'Seu nome é {nome}')

#     if nome == 'sair':
#         break

contador = 0

# Exemplo de laço de repetição, usando o operador de soma
while contador <= 20:
    contador += 1

    if contador == 3:
        print(f'Não irá aparecer o número {contador}')
        continue # Uso do continue para não parar o laço

    if contador >= 7 and contador <= 15:
        print(f'Não irá aparecer o número {contador}')
        continue # Uso do continue para não parar o laço

    print(contador)

    if contador == 20:
        break # Uso do break para parar o laço


print('Acabou o laço')