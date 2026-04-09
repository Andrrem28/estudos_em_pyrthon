''' while/else '''

string = 'Aqui tem um texto'

i = 0

while i < len(string):
    letra = string[i]

    print(letra)
    i += 1

    # O else em conjunto de um while, serve para caso eu tenha
    # alguma condição if dentro, para exibir uma mensagem de erro.

else:
    print('Mensagem de erro')

print('Fora do while')