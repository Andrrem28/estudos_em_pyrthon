'''
@staticmethods (métodos estáticos) são inúteis em Python 
Métodos estáticos são métodos que estão dentro da classe,
mas não tem acesso ao self e nem ao cls.
Em resumo, são funcções que existem dentro da sua classe.
'''
class MinhaClasse:
	@staticmethod
	def sua_funcao(*args, **kwargs):
		print('Ala!', args, kwargs )


c1 = MinhaClasse()
c1.sua_funcao(1, 2, 3)

MinhaClasse.sua_funcao(nomeado = 10)
