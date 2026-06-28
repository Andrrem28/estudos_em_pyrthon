import abc

# Extra: Aplicando tipagem
class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ... # metodo(self, attr: tipo) -> tipo aguardado: 

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('---###---###---')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}'
        return f'{class_name} {attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado.')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}'
        return f'{class_name} {attrs}'

class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0) -> None:
        super().__init__(agencia, conta, saldo) # Passando os valores pro __init__ da classe pai
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print(f'Seu limite é {-self.limite:.2f}')
        print('Não foi possível sacar o valor desejado.')
        self.detalhes(f'(SAQUE NEGADO {valor})')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r}'
        return f'{class_name} {attrs}'

if __name__ == '__main__':
    conta_poupanca = ContaPoupanca(111,222, 0)

    conta_poupanca.sacar(1)
    conta_poupanca.depositar(1)
    conta_poupanca.sacar(1)

    print('##')
    conta_corrente = ContaCorrente(111,222, 0, 100)

    conta_corrente.sacar(98)
    conta_corrente.depositar(1)
    conta_corrente.sacar(1)
    conta_corrente.sacar(90)