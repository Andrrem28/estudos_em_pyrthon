'''
Encapsulamento (modificãdores de acesso: public, private, protected)
Python NÃO TEM modificadores de acesso
Mas podemos seguir as seguintes convenções
(sem underline) = public
	pode ser usado em qualquer lugar
(com underline) = protected
	NÃO DEVE ser usado fora da classe ou suas classes.
(dois underlines) = private
	"name mangling" (desfiguração de nomes) em Python
	só deve ser usado na classe em que foi declarado.
'''

class Foo:
	def __init__(self):
		self.public = 'isso é público' # public
		self._protected = 'isso é protegido' # protected
		self.__private = 'isso é protegido' # private

	def metodo_publico(self):
		self._metodo_protected()
		self.__metodo_private()
		self._protected
		return 'metodo_publico'

	def _metodo_protected(self):
		return print('_metodo_protected')

	def __metodo_private(self):
		return print('__metodo_private')

f = Foo()
print(f.public)

print(f.metodo_publico())