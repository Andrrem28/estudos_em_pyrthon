# Conteúdo adicional sobre o yield

def gen1():
	print('Iniciou Gerador 1')
	yield 1
	yield 2
	yield 3
	yield 4
	print('Encerrado Gerador 1')

def gen2(gen):
	# yield from gen1()
	print('Iniciou Gerador 2')
	yield from gen()
	yield 5
	yield 6
	yield 7
	print('Encerrado Gerador 2')

def gen3():
	print('Iniciou Gerador 3')
	yield 8
	yield 9
	yield 10
	print('Encerrado Gerador 3')


g1 = gen2(gen1)
g2 = gen2(gen3)

for n in g1:
	print(n)

for n in g2:
	print(n)