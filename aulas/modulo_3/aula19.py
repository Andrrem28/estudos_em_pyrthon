'''
super() é a super classe na sub classe
Classe principal (Pessoa)
 -> super class, base class, parent class
Classe filha (Aluno)
    -> sub class, derived class, child class
'''

# class MinhaString(str):
#     def upper(self):
#         print('Chamando o método upper da classe MinhaString')
#         retorno = super().upper()
#         print('Retorno do método upper da classe str')
#         return retorno

# string = MinhaString('Olá, Mundo!')

# print(string.upper())

class A:
    atrubuto_a = 'Valor do atributo da classe A'

    def __init__(self, atributo):
        self.atrubuto = atributo
        print('Inicializando a classe A')
        print(f'Atributo: {atributo}')

    def falar(self):
        print('classe A falando...')

class B(A):
    atrubuto_b = 'Valor do atributo da classe B'

    def __init__(self, atributo, outro_valor):
        super().__init__(atributo)
        self.outro_valor = outro_valor
        print('Inicializando a classe B')
        print(f'Atributo: {atributo}, Outro valor: {outro_valor}')

    def falar(self):
        print('classe B falando...')

class C(B):
    atrubuto_c = 'Valor do atributo da classe C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Inicializando a classe C')

    def falar(self):
        super().falar()
        print('classe C falando...')

c = C('Valor do atributo', 'Valor do outro atributo')
c.outro_valor = 'Novo valor do outro atributo'
print(c.outro_valor)

# print(c.atrubuto_a)
# print(c.atrubuto_b)
# print(c.atrubuto_c)

# c.falar()