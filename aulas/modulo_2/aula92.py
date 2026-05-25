# Generator expression, Itables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter_ e __next__

# print(next(iterator))
import sys

lista = [n for n in range(100)]
generator = (n for n in range(100)) # Generator Expression

'''
Obs: A diferença entre a lista e o generator, é que a lista
já esta carregada na memória, já o generator não, pois ele precisa 
de um comando para poder acessar os valores.
'''

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))

for n in generator:
	print(n)
