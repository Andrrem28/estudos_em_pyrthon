'''
Herança simples - Relações entre classes
Associação - usa, Agregação - tem
Composição - é dono de, Herança - é um

Herança ou Composição

Classe principal (Pessoa)
 -> super class, base class, parent class
Classe filhas (Cliente, Funcionario)
 -> sub class, child class, derived class
'''

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_sobrenome(self):
        return print(f'{self.nome} {self.sobrenome}, {self.__class__.__name__}')

class Cliente(Pessoa):
    ...

class Funcionario(Pessoa):
    ...

cliente  = Cliente('Luiz', 'Otávio')
funcionario = Funcionario('Maria', 'Oliveira')

cliente.falar_nome_sobrenome()
funcionario.falar_nome_sobrenome()