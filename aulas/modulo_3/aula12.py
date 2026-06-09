'''
@property + @setter - getter e setter no modo Pythonico
- como getter
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
Atributos que começa com um ou dois underlines, não devem
ser usado fora da classe.
'''

class Caneta:
	def __init__(self, cor):
		# self.cor_tinta = cor
		self.cor = cor
		self._cor_tampa = None

	@property
	def cor(self):
		return self._cor

	@cor.setter
	def cor(self, valor):
		print('Estou no setter', valor)
		self._cor = valor

	@property
	def cor_tampa(self):
		return self._cor_tampa


	@cor_tampa.setter
	def cor_tampa(self, valor):
		self._cor_tampa = valor


def exibir(caneta):
	return caneta.cor

caneta = Caneta('Preta')
caneta.cor = 'Vermelha' # aplicando o @cor.setter nesse momento
caneta._cor_tampa = 'Azul'

print(caneta._cor_tampa)
# getter -> obtém valor



