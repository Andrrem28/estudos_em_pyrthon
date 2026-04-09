'''
Exercício
Iterando strings com o uso do while
'''

nome = 'André Martins' 

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice] # O uso da variável indice como chave do array. Vai servir para acessar o valor em cada laço da iteração.

    novo_nome += f'*{letra}'

    indice += 1

novo_nome += '*'
print(novo_nome)
