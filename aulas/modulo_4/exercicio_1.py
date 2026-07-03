# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime

from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000

data_emprestimo = datetime(2026, 7, 5) # Data do empréstimo
delta_anos = relativedelta(years = 4) # Duração do empréstimo em anos
data_final = data_emprestimo + delta_anos # Data final do empréstimo

data_parcelas = []
data_parcela = data_emprestimo

while data_parcela <= data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_emprestimo / numero_parcelas

for data_pagamento_parcela in data_parcelas:
    print(f"Data de vencimento: {data_pagamento_parcela.strftime('%d/%m/%Y')} - Valor da parcela: {valor_emprestimo / len(data_parcelas):.2f}")

print(numero_parcelas, f"{valor_parcela:,.2f}")