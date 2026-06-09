'''
@property - um getter no modo Pythônico
getter - um método para obter um atributo
modo pythônico - modo do Python de fazer coisas.

@property é uma propriedade do objeto, ela
é um método que se comporta como um atributo (blow mind)
Geralmente é usada nas seguintes situações:
- como getter
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo

Código cliente - é o código que usa o seu código.
'''

# class Caneta:
# 	def __init__(self, cor_tinta):
# 		self.cor_tinta = cor_tinta

# 	def get_cor(self):
# 		print('Get Cor')
# 		return self.cor_tinta

# ## -- Código cliente -- ##

# caneta = Caneta("Preta")

# print(caneta.get_cor())

# ## --  -- ##

class Caneta:
	def __init__(self, cor, tampa):
		self.cor_tinta = cor
		self.cor_tampa = tampa

	@property
	def cor(self):
		return self.cor_tinta

	@property
	def tampa(self):
		return self.cor_tampa
	

caneta = Caneta('Preta', 'Azul')

print(caneta.cor, caneta.cor_tampa)