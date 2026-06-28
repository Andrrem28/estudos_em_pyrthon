import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self) -> int:
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.nome!r}, {self.idade!r}'
        return f'{class_name} {attrs}'

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == '__main__':
    cliente = Cliente('André', 36)

    cliente.conta = contas.ContaCorrente(111, 222, 0, 0)

    print(cliente)
    print(cliente.conta)

    cliente_2 = Cliente('André', 36)

    cliente_2.conta = contas.ContaCorrente(111, 222, 0, 0)

    print(cliente_2)
    print(cliente_2.conta)