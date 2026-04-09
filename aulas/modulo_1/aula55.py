'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
'''

import os

lista_de_compras = []

while True:
    print('Selecione uma opção: ')

    opcao = input('[i]nserir, [a]pagar, [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        
        valor = input('Valor: ')
        lista_de_compras.append(valor)
        
    elif opcao == 'a':
        for i, valor in enumerate(lista_de_compras):
                print(i, valor)

        indice_str = input('Escola o índice para apagar: ')
                
        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
        except ValueError:
            print('Por favor digite apenas números inteiros.')
        except IndexError:
            print('Não foi possível localizar o item na lista.')
        except Exception:
            print('Erro desconhecido.')
    elif opcao == 'l':
        os.system('clear')

        if len(lista_de_compras) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista_de_compras):
            print(i, valor)

