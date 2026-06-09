'''
Relações entre classes: associação, agregação e composição.
Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.
Essa é a relação mais comum entre objetos e tem subconjuntos como agregação e composição (que veremos depois).
Geralmente, temos uma associação quando um objetotem um atributo que referência outro objeto.

A associação não especifica como um objeto controla o ciclo de vida de um outro objeto.
'''

class Escritor:
	def __init__(self, nome) -> None:
		self.nome = nome
		self._ferramenta = None

	@property
	def ferramenta(self):
		return self._ferramenta # protected


	@ferramenta.setter
	def ferramenta(self, ferramenta):
		self._ferramenta = ferramenta

class FerramentaDeEscrever:
	def __init__(self, nome):
		self.nome = nome


	def escrever(self):
		return f'{self.nome} está escrevendo.'

escritor = Escritor('André')
caneta = FerramentaDeEscrever('Lápis')
maquina = FerramentaDeEscrever('Maquina')

escritor.ferramenta = caneta
escritor.ferramenta = maquina

print(caneta.escrever())
print(maquina.escrever())
print(escritor.ferramenta.escrever())
