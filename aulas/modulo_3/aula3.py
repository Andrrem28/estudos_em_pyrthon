# Escopo da classe e de métodos da classe
class Animal(object):

	#
	def __init__(self, nome):
		self.nome = nome
	#	

	def acao(self, alimento):
		# Dentro do escopo da classe, é possível usar o self do método para poder
		# ter acesso ao valor do atributo do objeto da classe íniciado no método __init__
		return print(f'{self.nome} está comendo sua {alimento}')

	def bebendo_agua(self, *args, **kwargs):
		return self.acao(*args, **kwargs)


animal = Animal('Cachorro')

animal.acao('ração')
animal.bebendo_agua('O Cachorro esta bebendo água.')

print(animal.nome)
