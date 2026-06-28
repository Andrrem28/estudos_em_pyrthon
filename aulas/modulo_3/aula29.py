# Context Manager com função - Criando e Usando gerenciadores de contexto

from contextlib import contextmanager

@contextmanager
def my_open(carminho_arquivo, modo):
    try:
        print('Abrindo o arquivo')
        arquivo = open(carminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu algum erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with my_open('aula29.py', 'w') as arquivo:
    arquivo.write('Linha 1 \n')
    arquivo.write('Linha 2 \n')
    arquivo.write('Linha 3 \n')
    print('WITH', arquivo)