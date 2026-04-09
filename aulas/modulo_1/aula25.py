'''
Interporlação básica de strings
s - string
d e i - int
f - float 
x e X Hexadecimal (ABCDEF019238)
'''

nome = 'André'
preco = 1000.987863
# Ex: Usando a interpolação, aplicando dois valores.
# caso seja usado apenas um, não precisa por os (), basta
# por o nome da variável que deseja exibir o valor dela.
# Obs: %.2f é para formatar o resultado com ponto flutuante, para duas casas decimais.
variavel = '%s, o preço é R$%.2f' % (nome, preco) # Caso coloque um terceiro valor, mas ele não tenha sido declarado anteriormente, ele irá quebrar.
print(variavel)
# Obs: Para o Hexadecimal, se você colocar x ele vai mostrar mínusculo o resultado,
# se colocar o X, ele irá exibir maiúsculo.
print('O Hexadecimal de %d é %08x' % (1500, 1500))