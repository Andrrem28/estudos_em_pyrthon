'''
Clousure e funções que retornam outras funções
'''

def criar_saudacao(saudacao, nome):
	def saudar(sobrenome):
		return f'{saudacao}, {nome} {sobrenome}'
	return saudar



fun_1 = criar_saudacao('Boa noite', 'André')
fun_2 = criar_saudacao('Boa tarde', 'André')

print(fun_1)
print(fun_2('Martins')) # Uso de Clousure, com o seu parametro, adiantando a função.