# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field, fields

@dataclass 
class Pessoa:
    nome: str = field(default='Não tem', repr=False) # Pode se passar valores nos argumentos para desativar alguns outros dunder methods
    sobrenome: str = 'Não tem também'
    idade: int = 0
    enderecos: list[str] = field(default_factory = list)

if __name__ == '__main__':
    p1 = Pessoa('André', 'Freitas', 36)
    p2 = Pessoa('Jacksielli', 'Freitas', 30)

    print(p1, p2)