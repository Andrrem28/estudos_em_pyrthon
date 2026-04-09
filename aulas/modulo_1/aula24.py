# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 
# A n d r é
# -5 -4 -3 -2 -1 # Pode consultar por número negativo

# nome = 'André'
# print(nome[2])
# print(nome[-3])
# Ex: Pode se usar não só um caractere, mas vários em uma mesma consulta.
# print('q' in nome) # False
# print('q' not in nome) # True

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
