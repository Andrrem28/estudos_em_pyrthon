'''
Controlando a quantidade de argumentos posicionais e nomeados em funções
*args (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)
Positional-only Parameters (/) - Tudo antes da barra deve ser ! APENAS ! posicional.
PEP 570 - Python Positional-Only Parameters
Keyword-Only Arguments (*) - * sozinho !NÃO SUGA! valores.
PEP 3102 - Keyword-Only Arguments
'''

def soma(a, b, /, x, y): # 
	print(a + b + x + y)

soma(1, 4, 5, 7)

# def soma(a, b, *, x):
# 	print(a + b + x)

# soma(1, 4, x = 5)