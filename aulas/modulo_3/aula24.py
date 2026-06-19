'''
Polimorfismo em Python Orientado a Objetos
Polimorfismo é o princípio que permite que
classes derivadas de uma mesma superclasse
tenham métodos iguais (com mesma assinatura)
mas comportamentos diferentes.

Assinatura do método = Mesmo nome e quantidade de parâmetros (retorno não faz parte da assinatura)
Opinião + princípio que contam: nome, parâmetros e retornos iguais SO"L"ID
Princípio da substituição de Liskov: 
    objetos de uma classe derivada devem ser substituíveis por objetos da classe base sem alterar o comportamento do programa.

Sobrecarga de métodos:
    Python não suporta sobrecarga de métodos como em outras linguagens, mas podemos simular isso usando argumentos padrão ou *args e **kwargs.

Sobrescrita de métodos:
    Em Python, a sobrescrita de métodos é feita simplesmente definindo um método com o mesmo nome na classe derivada. O método da classe derivada irá substituir o método da classe base quando chamado em uma instância da classe derivada.
'''
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ... # Lógica para enviar a notificação

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'Enviando email com a mensagem: {self.mensagem}')
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f'Enviando SMS com a mensagem: {self.mensagem}')
        return True


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada com sucesso!')
    else:
        print('Falha ao enviar a notificação!')

notificar(NotificacaoEmail('Mesnagem do tipo e-mail'))

notificar(NotificacaoSMS('Mesnagem do tipo SMS'))