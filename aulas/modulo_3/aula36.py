# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import asdict, astuple, dataclass

@dataclass(init=False) # Caso queira que o dunder methods, só passar no argumento do @dataclass() 
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    # def __post_init__(self):
    #     self.nome_completo = f'Meu nome é {self.nome} {self.sobrenome} e tenho {self.idade} anos.'
    #     print('Pós init')

    # def nome_completo(self):
    #     return f'Meu nome é {self.nome} {self.sobrenome} e tenho {self.idade} anos.'

if __name__ == '__main__':
    p1 = Pessoa('André', 'Freitas', 36)
    p2 = Pessoa('Jacksielli', 'Freitas', 30)

    # print(asdict(p1).keys())
    # print(asdict(p2).keys())
    # print(asdict(p1).values())
    # print(asdict(p2).values())
    # print(asdict(p1).items())
    # print(asdict(p2).items())
    # print(astuple(p1)[0])
    # print(astuple(p2)[0])

    # print(p1.nome_completo())
    # print(p2.nome_completo())