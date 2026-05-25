# Aula 73

'''
Higher Order Functions
Funções de primeira classe
'''

def hello(msg, nome):
	return f'{msg}, {nome}'

# Uma função que executa outras funções, passada por parâmetro.
def executa(funcao, *args):
	return funcao(*args)


msg_1 = hello # A função hello, não está sendo executada, mas sim atribuida a uma variável, assim tornando ela a mesma coisa da função.

v = msg_1('Estou sendo executado pela variável msg_1', 'André')

msg_2 = hello('Estou sendo executado pela própria chamda da função hello()', 'André')

exec_1 = executa(msg_1, 'Estou sendo executada via função executa', 'André')


print(v)

print(exec_1)

print(msg_2)