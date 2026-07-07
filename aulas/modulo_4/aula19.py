# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale
import string
from datetime import datetime
from pathlib import Path

locale.setlocale(locale.LC_ALL,'')

def converte_para_brl(numero: float) -> str:
    """Converte um número para o formato monetário brasileiro."""
    brl = "R$ " + locale.currency(numero, symbol = False, grouping = True)

    return brl

data = datetime.now()

dados = dict(
    nome = "André",
    valor = converte_para_brl(1_414_241),
    data = data.strftime("%d/%m/%Y"),
    empresa = 'Tanto Faz Soluções em TI',
    telefone = '+55 (11) 99999-9999'
)

with open(Path(__file__).parent / "aula19_template.txt", "r", encoding="utf-8") as arquivo:
    template = string.Template(arquivo.read())
    
    print(template.substitute(dados))