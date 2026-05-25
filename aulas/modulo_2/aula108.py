# count é um iterador sem fim (itertools)
from itertools import count

count_1 = count(10, 8) # pode se passar kwargs e arumentos nomeados.

# print(next(count_1))

print('count_1', hasattr(count_1,'__iter__'))

for i in count_1:
	if i >= 100:
		break

	print(i)	
