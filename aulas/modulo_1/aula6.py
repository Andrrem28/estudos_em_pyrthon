'''
Conversão de tipos, coreção
type convertion, typecasting, coercion 
é o ato de converter um tipo em outro
tipos imutáveis e primitivos:
str, int, float, bool
'''
# Usando a class/function int, para conversão de números, do tipo strig para inteiro.
print('Conversão de str > int')
print('1', type('1'))
print(type(int('1')))
print(int('1') + 1)
# Usando a class/function float, para conversão de números, do tipo strig para float.
print('Conversão de str > float')
print('1', type('1'))
print(type(float('1')))
print(float('1') + 1)
# Usando a class/function string, para conversão de números, do tipo int para str.
print(type(11))
print(type(str(11)))
print(str(11) + 'A') # Aqui nesta situação, irá ocorrer uma concatenação das string
# Usando a class/function float, para conversão de números, do tipo str para bool.
print(bool(' '))
print(type(bool(' ')))