# Atributos de classe
class Pessoa:
	ano_vigente = 2026

	def  __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def ano_de_nascimento(self):
		# return self.ano_vigente - self.idade (Desta forma implicará um problema no método, pois o self, irá verificar primeiro a instância (__init__), para depois verificar o 
		# o valor do atributo da classe)
		return Pessoa.ano_vigente - self.idade


p1 = Pessoa('André', 36)

