'''
Herança Multipla - Python Orientado a Objetos
Quer dizer que no Python, uma classe pode estender (herdar) várias outras classes.
Herança Simples:
Animal -> Mamifero -> Humano -> Pessoa -> Cliente
Herança Multipla:
Log -> FileLog
Cliente(Pessoa, FileLog)

Python 3 usa C3 superclass linearization para resolver a ordem de herança (mro)

Para saber a ordem de chamada dos métodos, podemos usar o método mro() ou o atributo __mro__ da classe.
'''

class A:
    ...

    def quem_sou(self):
        print('Falando de A')

class B(A):
    ...

    def quem_sou(self):
        print('Falando de B')

class C(A):
    ...

    def quem_sou(self):
        print('Falando de C')


class D(B, C):
    ...

    def quem_sou(self):
        print('Falando de D')

d = D()
d.quem_sou()

print(D.mro())