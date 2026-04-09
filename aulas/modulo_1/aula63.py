'''
Melhorias no código de checagem de dígitos.
'''

import re as ex_regular
import sys

# cpf_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace('-', '') \
#     .replace(' ', '')

cpf_enrtada = input('Digite o seu CPF: ')

cpf_usuario = ex_regular.sub(
        r'[^0-9]',
        '',
        cpf_enrtada
    )

val_sequencial = cpf_enrtada == cpf_enrtada[0] * len(cpf_enrtada)

if val_sequencial:
    print('Você mandou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_usuario[:9]

con_regrevisso_1 = 10

res_digito_1 = 0

for digito in nove_digitos:
    res_digito_1 += int(digito) * con_regrevisso_1

    con_regrevisso_1 -= 1

digito_1 = (res_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
con_regrevisso_2 = 11


res_digito_2 = 0

for digito in dez_digitos:
    res_digito_2 += int(digito) * con_regrevisso_2

    con_regrevisso_2 -= 1   
     
digito_2 = (res_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_completo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_usuario == cpf_completo:
    print(f'{cpf_usuario} é válido.')
else:
    print('CPF inválido.')