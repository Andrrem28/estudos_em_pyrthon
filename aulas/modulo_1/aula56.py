'''
Imprecisão de ponto flutuante
Double-precision, floating-point, format, IEEE, 754
'''

import decimal as dc

# n1 = 0.1
# n2 = 0.7

n1 = dc.Decimal('0.1')
n2 = dc.Decimal('0.7')

n3 = n1 + n2

# print(n3)
# print(f'{n3:.2f}') # retorna um str -> 0.80
# print(round(n3, 2)) # retorna um int -> 0.8
