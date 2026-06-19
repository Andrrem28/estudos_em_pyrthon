'''
Criando Exceptions em Python Orientado a Objetos
Para criar uma Exception em Python, você só precisa herdar de alguma exceção da linguagem.
A recomendação é herdar de Exception ou de alguma classe que herde de Exception, como ValueError, TypeError, etc.
Criando exceções (comum colocar Error no final)
Levantando (raise) e tratando (try/except) exceções
Relançamento exceções (raise sem argumentos dentro do except)
'''

class MyError(Exception):
    pass

class OtherError(Exception):
    pass

def up():
    exception_ = MyError('Erro 1', 'Erro 2', 'Erro 3')
    exception_.add_note('Nota 1')
    exception_.add_note('Nota 2')
    raise exception_

try:
    up()
except (MyError, ZeroDivisionError) as e:
    print(e.__class__.__name__)  # Imprime a classe da exceção
    print(f'Erro capturado: {e.args}')  # Imprime os argumentos da exceção
    exception_ = OtherError('Outro erro ocorreu')  # Cria uma nova exceção
    raise  exception_ from e# Relança a exceção para ser tratada em outro lugar ou para encerrar o programa