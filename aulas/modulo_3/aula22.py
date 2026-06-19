'''
Classes Abstratas - Abstract Base Classes (ABC)
ABCs são usadas como contratos para a definição
de novas classes. Elas podem forçar outras classes a criarem métodos concretos.
Também podem ter métodos concretos por elas mesmas.

@abstractmethod são métodos que não tem corpo.
As regras para classes abstratas com métodos abstratos é que elas NÃO PODEM SER INSTANCIADAS, ou seja, não podem criar objetos.

Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod).

Uma classe abstrata em Python tem suas metaclasse definida como ABCMeta, e os métodos abstratos são decorados com @abstractmethod.

É possível criar: 
    @property; 
    @setter; 
    @classmethod;
    @staticmethod;
    @method;

Como abstratos, para isso use @abstractmethod como decorador mais interno.
'''
from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, message): ... # método abstrato, sem corpo

    def log_error(self, message):
        self._log(f"ERROR: {message}")

    def log_success(self, message):
        self._log(f"SUCCESS: {message}")

class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} ({self.__class__.__name__})')

    
l = LogPrintMixin()
l.log_error("Erro ao processar o arquivo")

