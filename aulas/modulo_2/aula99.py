# Aula 99
import importlib 

import aula99_m

for i in range(10):
	importlib.reload(aula99_m)
	print(i)

print(aula99_m.var_modulo)