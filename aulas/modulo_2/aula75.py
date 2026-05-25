'''
Exercícios 
Crie funções que duplicam, triplicam e quadriplicam
o número recebido como parâmetro.
'''

def criar_multiplicador(multiplicador):
	def multiplicar(numero):
		return numero * multiplicador
	return multiplicar


# Chamada da função criar_multiplicador, passando o valor do parâmetro que será o multiplicador, da função multiplicar.
duplicar = criar_multiplicador(2) # 
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))