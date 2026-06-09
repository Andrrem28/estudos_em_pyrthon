'''
Relações entre classes: associação, agregação e composição.
Agregração é uma forma mais especializada de assosciação entre dois ou mais objetos.
Cada objeto terá seu ciclo de vida independente.
Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.
Os objetos podem viver separadamente, mas pode setratar de uma relação onde um objeto
precisa de outro para fazer determinada tarefa.
(Existem controversias sobre as definições de agregação.)
'''

class CarrinhoCompra:
	def __init__(self):
		self._produtos = []


	def preco_total(self):
		return sum([produto.preco for produto in self._produtos])


	def adicionar_produto(self, *produtos):
		# Três formas diferentes par ao mesmo resultado.
		self._produtos.extend(produtos) 
		# self._produtos += produtos
		# for produto in produtos:
			# self._produtos.append(produtos)


	def listar_produtos(self):
		print()
		for produto in self._produtos:
			print(produto.nome, produto.preco)
		print()



class Produto:
	def __init__(self, nome, preco):
		self.nome = nome
		self.preco = preco


carrinho = CarrinhoCompra()

p1, p2 = Produto('Caneta', 1.20), Produto('Camisa', 7.00)

carrinho.adicionar_produto(p1, p2)

carrinho.listar_produtos()

print(f'Total: {carrinho.preco_total()}')