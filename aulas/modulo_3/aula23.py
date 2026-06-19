'''
abstractmethod para qualquer método já decorado.
É possível criar @property, @property.setter, @classmethod, @staticmethod e métodos normais como abstratos, 
para isso use @abstractmethod antes do decorador (decorator) específico/mais interno.

Foo - Bar são palavras usadas como placeholder, para palavras que podem mudar na programação.
'''
from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = name # Deve ser definido como atributo privado e antes do setter, para evitar que seja sobrescrito diretamente, e sim usando o setter.
        self.name = name

    # @property
    # @abstractmethod
    # def name(self): ...
   
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name): ...

class Foo(AbstractFoo):
    name = '' # Funciona desta forma também, mas é mais recomendado usar o atributo privado e o setter para evitar que seja sobrescrito diretamente, e sim usando o setter.
    
    def __init__(self, name):
        super().__init__(name)
        # print('Sou uma classe sem uso')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, name):
    #     self._name = name

        
foo = Foo('Foo')
print(foo.name)