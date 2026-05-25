# Variáveis livres + nonlocal (locals, globals)
#  print(globals()) # Exibe todas as variáveis globais
# def escopo_a(x):
# 	a = x # variável livre, dentro do escopo_a

# 	def escopo_b():
# 		# print(locals())
# 		print(escopo_b.__code__.co_freevars)
# 		return a 
# 	return escopo_b


# escopo_b = escopo_a(5)
# escopo_b2 = escopo_a(10)

# print(escopo_b())
# print(escopo_b2())

def unifica_coisas(string_inicial):
	valor_final = string_inicial

	def funcao_interna(valor_a_concatenar):
		nonlocal valor_final # O nonlocal pega o valor da variável livre de fora do escopo onde foi declarada.
		valor_final += valor_a_concatenar
		return valor_final

	return funcao_interna

exec_f = unifica_coisas('a')

print(exec_f('b'))
