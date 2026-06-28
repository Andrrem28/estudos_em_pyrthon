'''
Classes decoradoras (Decorator classes)
'''

class Multiplicador:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador # Valor inicial


    def __call__(self, func, *args, **kwargs):
        def func_interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
           
            return resultado * self._multiplicador
        return func_interna

@Multiplicador(20)
def soma(x,y):
    return x + y

soma_numeros = soma(2, 5)

print(soma_numeros)
