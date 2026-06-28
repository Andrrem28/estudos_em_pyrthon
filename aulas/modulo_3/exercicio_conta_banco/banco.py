import contas
import pessoas

class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None,
        ) -> None:
        self.clientes = clientes or []
        self.agencias = agencias or []
        self.contas = contas or []

    def _verifica_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _verifica_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _verifica_conta(self, conta):
        if conta in self.contas:
            return True
        return False
    
    def _verifica_veracidade_da_conta(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._verifica_agencia(conta) and \
            self._verifica_cliente(cliente) and \
            self._verifica_conta(conta) and \
            self._verifica_veracidade_da_conta(cliente, conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencias!r}, {self.clientes!r}, {self.contas!r}'
        return f'{class_name} {attrs}'
    

if __name__ == '__main__':
   cliente_1 = pessoas.Cliente('André', 36)
   conta_c = contas.ContaCorrente(111,222,0,0)

   cliente_1.conta = conta_c

   cliente_2 = pessoas.Cliente('Jacksielli', 30)
   conta_p = contas.ContaPoupanca(111,222,100)

   cliente_2.conta = conta_p

   banco = Banco()
   banco.clientes.extend([cliente_1, cliente_2])
   banco.contas.extend([conta_c, conta_p])
   banco.agencias.extend([111, 222])
   
   print(banco.autenticar(cliente_1, conta_c))
   print(banco)

   if banco.autenticar(cliente_1, conta_c):
       conta_c.depositar(10)
       print(cliente_1.conta)