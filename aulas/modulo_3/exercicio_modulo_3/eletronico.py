from log import LogFileMixin

class Eletronico:
    # código da classe Eletronico
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            print(f"{self._nome} ligado.")
    
    def desligar(self):
        if self._ligado:
            self._ligado = False
            print(f"{self._nome} desligado.")


class Smartphone(Eletronico, LogFileMixin):
    # código da classe Smartphone
    def ligar(self):
        super().ligar()

        if self._ligado:
            self.log_success(f"{self._nome} foi ligado.")


    def desligar(self):
       super().desligar()

       if not self._ligado:
           self.log_success(f"{self._nome} foi desligado.")