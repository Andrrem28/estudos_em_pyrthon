'''
Flag (Bandeira) - Marcar um local
Nome = Não Valor
is e is not = é ou não é (tipo, valor, identidade)
id() = Identidade
'''

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo', id(condicao)) # A função id, mostra o identificador da variável na memória
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')