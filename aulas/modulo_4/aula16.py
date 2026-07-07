# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula16.csv'

lista_de_clientes = [
    {'nome': 'André', 'endereco': 'Av 1, 22'},
    {'nome': 'João Silva', 'endereco': 'R. 2, "1"'},
    {'nome': 'Maria Sol', 'endereco': 'Av B, 3A'}
]

with open(CAMINHO_CSV, 'w', newline = '') as arquivo_csv:
    nome_colunas = lista_de_clientes[0].keys()
   
    escritor = csv.DictWriter(arquivo_csv, fieldnames=nome_colunas)
    escritor.writeheader()
    
    # colunas = ['nome', 'endereco']
    # escritor.writerows(lista_de_clientes)

    for cliente in lista_de_clientes:
        escritor.writerow(cliente)
