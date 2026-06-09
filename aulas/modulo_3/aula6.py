# __dict__ e vars para atributos de instância
class Pessoa:
	ano_vigente = 2026

	def  __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

	def ano_de_nascimento(self):
		return Pessoa.ano_vigente - self.idade

dados = {'nome': 'André', 'idade': 36}

# p1 = Pessoa(**dados) # Desempacotando os valores da variável dados
p1 = Pessoa('André', 36)

# print(vars(p1))

print(p1.nome, p1.idade)

# p1.__dict__['nova_chave'] = 'Novo valor' # Adicionando uma nova chave ao meu dicionário
# print(p1.__dict__) 
# print(vars(p1)) # O método vars, é a mesma coisa que usar o __dict__
# del p1.__dict__['nova_chave'] # removendo a chave nova_chave do dicionário.
# print(p1.nova_chave)

