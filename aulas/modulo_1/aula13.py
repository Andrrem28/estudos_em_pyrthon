# Formatação de texto, usando a f-strings
nome = 'André Martins'
altura = 1.80
peso = 90
imc = 90 / altura ** 2
# Ex: Abaixo vemos que podemos usar todo o conteúdo de uma vairável
# dentro de uma única string, contanto que tenha um f fora do inicio da abertura da
# string, junto dos {var}, para que seja renderizado o resultado.
# Obs: var:.2f, é para formatar as casas decimais.

linha_1 = f'{nome} tem {altura:.2f} de altura pesa {peso} quilos e seu IMC é {imc:.2f}'

print(linha_1)