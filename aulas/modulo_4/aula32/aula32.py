# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path
from pypdf import PdfReader, PdfWriter
from datetime import datetime

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGEM = PASTA_RAIZ / 'pdfs'
NOVA_PASTA = PASTA_RAIZ  / 'novos_arquivos'

RELATORIO_BC = PASTA_ORIGEM / 'bc-relatorio-foco.pdf'
NOVA_PASTA.mkdir(exist_ok = True)

reader = PdfReader(RELATORIO_BC)

# print(len(reader.pages))
# for page in reader.pages:
    # print(page)

page0 = reader.pages[0]
image_0 = page0.images[0]

# print(page0.extract_text())
# with open(NOVA_PASTA / image_0.name, 'wb') as fp:
#     fp.write(image_0.data)

# writer = PdfWriter()

# with(open(NOVA_PASTA / 'NOVO_ARQUIVO_PDF.pdf', 'wb')) as arquivo:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(arquivo)

for i, page in enumerate(reader.pages):
    with(open(NOVA_PASTA / f'page_{i}.pdf', 'wb')) as arquivo:
        writer = PdfWriter()
        writer.add_page(page)
        writer.write(arquivo)