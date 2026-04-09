# Uso da função input, com f-string para exibição do valor da variável. 
# Caso queira aparecer o nome da variável junto do seu valor, basta por um = a frente
# da variável no output do resultado. Ex: var=
# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

# Uso da função input, para soma de dois números, usando coerção.
# Aqui se aplica apenas a exemplo de estudos, de como funciona a função,
# pois, se eu colocar um caractere que não seja um número, o meu programa vai quebrar.
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

int_n1 = int(n1)
int_n2 = int(n2)

print(f'A soma dos dois números é {int_n1 + int_n2}')