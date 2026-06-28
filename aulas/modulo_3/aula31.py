'''
Método especial __call__
callable é algo que pode ser executado com parênteses
Em classes normais, __call__ faz instância de uma classe "callable.
'''

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome, *args, **kwargs):
        print(nome, ' está chamando', self.phone)

        # return 1231

call_1 = CallMe('123123')

call_1('André Martins')