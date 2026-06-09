# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro parâmetro,
# receberemos a própria classe.

class Pessoa:
	ano = 2026 # Atributo de classe

	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	@classmethod
	def say_hello(cls): # cls é o mesmo que usar Pessoa (Nome da classe)
		return print(f"Olá")

	@classmethod
	def criar_com_50_anos(cls, nome): 
		return cls(nome, 50) # Hard Corder

	@classmethod
	def criar_sem_nome(cls, nome): 	
		return cls(nome, 24) # Hard Corder

# print(Pessoa.ano) # Atributo da classe

p1 = Pessoa('André', 36)
p1.say_hello() # Usando o objeto para a chamada do método da classe Pessoa.

p2 = Pessoa.criar_com_50_anos('André') # Método fabricado
print(p2.nome, p2.idade)

p3 = Pessoa.criar_sem_nome('Anônimo')
print(p3.nome, p3.idade)

# Pessoa.say_hello() # Usando o nome da própria classe para chamar o método.