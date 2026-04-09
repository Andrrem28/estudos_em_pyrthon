'''
Criando um gerador de CPF's.
'''

import random 

# for _ in range(10): # Descomentar essa linha caso queira gerar mais de um CPF
digitos = '' 

for digito in range(9):
    digitos += str(random.randint(0, 9))

primeiro_cont_regressivo = 10

res_digito_1 = 0

for digito in digitos:
    res_digito_1 += int(digito) * primeiro_cont_regressivo
    primeiro_cont_regressivo -= 1

primeiro_digito = (res_digito_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

decimo_digito = digitos + str(primeiro_digito)

segundo_cont_regressivo = 11

res_digito_2 = 0

for digito in decimo_digito:
    res_digito_2 += int(digito) * segundo_cont_regressivo
    segundo_cont_regressivo -= 1

segundo_digito = (res_digito_2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado = f'{digitos}{primeiro_digito}{segundo_digito}'

print(cpf_gerado)
