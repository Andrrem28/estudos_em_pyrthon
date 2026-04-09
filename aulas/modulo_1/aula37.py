'''
Repetições
while + while (while com while interno)
Executa uma ação enquanto uma condição for verdadeira.
Loop infinito -> Quando um código não tem fim.
Obs.: Criar uma variável que irá ser o contador do seu laço, para que não se torne um laço infinito de repetição.
'''

qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1
    print(f'Linha de número {linha}')

    while coluna <= qtd_colunas:
        coluna += 1
        print(f'Coluna de número {coluna}')

    linha += 1

print('Acabou o laço')