# Introdução as Generator functions em Python
# generator = (n for n in range(100))

def generator(n = 0, maximum = 10):
	while True:
		yield n

		n += 1

		if n > maximum:
			return print('Laço encerrado!')

	# yield 1
	# print('Continuando...')
	# yield 2
	# print('Continuando...')
	# yield 3
	# return 'Encerrado'

gen = generator(maximum = 20)

for n in gen:
	print(n)

