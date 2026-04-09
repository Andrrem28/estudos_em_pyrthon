'''
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(<>)(quantidade)
= - Força o número a aparecer antes dos zeros
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0 >- 100,.1f
Conversion flags - !r !s !a
'''

var = 'ABC'
print(f'{var}')
print(f'{var:_>10}') # _______ABC
print(f'{var:_<10}') # ABC_______
print(f'{var:_^10}') # ___ABC____
print(f'{1000.6516516510615:0=+10,.1f}') # +001,000.7
print(f'O Hexadecimal de 1500 é {1500:08X}') # O Hexadecimal de 1500 é 000005DC