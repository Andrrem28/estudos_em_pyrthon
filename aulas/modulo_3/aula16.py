'''
Relações entre classes: associação, agregação e composição.
Composição é uma especialização da agregração.
Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos
também são apagadas.
'''

class Cliente:
	def __init__(self, nome):
		self.nome = nome
		self.enderecos = []

	def inserir_endereco(self, nome_rua, numero, bairro):
		self.enderecos.append(Endereco(nome_rua, numero, bairro))


	def inserir_endereco_externo(self, endereco):
		self.enderecos.append(endereco)

	def listar_enderecos(self):
		for endereco in self.enderecos:
			print(endereco.nome_rua, endereco.numero, endereco.bairro)

	def __del__(self):
		print('APAGANDO', self.nome)


class Endereco:
	def __init__(self, nome_rua, numero, bairro):
		self.nome_rua = nome_rua
		self.numero = numero
		self.bairro = bairro

	def __del__(self):
		print('APAGANDO', self.nome_rua, self.numero, self.bairro)


cliente = Cliente('André')

cliente.inserir_endereco('Dolores', 121, 'Abolição')
cliente.inserir_endereco('Maria', 51, 'Abolição')
cliente.listar_enderecos()
endereco_externo = Endereco('Av João da Escóssia', 1312, 'Nova Betânia')

print('Encerra aqui')

print(endereco_externo.nome_rua, endereco_externo.numero, endereco_externo.bairro)