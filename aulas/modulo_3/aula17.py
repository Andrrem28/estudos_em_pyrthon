'''
Exercício com classes

1 - Crie uma classe com o nome Carro (Nome)
2 - Crie uma classe Motor (Nome)
3 - Crie uma classe Fabricante (Nome)
4 - Faça uma ligação entre Carro e Motor (composição)
Obs: Um motor pode ser de vários carros.
5 - Faça uma ligação entre Carro e Fabricante (agregação)
Obs: Um fabricante pode fabricar vários carros.

Exiba o nome do carro, motor e fabricante na tela.
'''

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
fusca.motor = Motor('Motor 1.0')
fusca.fabricante = Fabricante('Volkswagen')

uno = Carro('Uno')
uno.motor = fusca.motor
uno.fabricante = Fabricante('Fiat')

print(f'Carro: {uno.nome}, Motor: {uno.motor.nome}, Fabricante: {uno.fabricante.nome}')
print(f'Carro: {fusca.nome}, Motor: {fusca.motor.nome}, Fabricante: {fusca.fabricante.nome}')