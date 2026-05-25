# Exercício - Sistema de perguntas e respostas.

perguntas = [
	{
		'pergunta' : 'Quanto é 2 + 2',
		'opcoes' : ['1', '3', '4', '5'],
		'resposta' : '4',
	},	
	{
		'pergunta' : 'Quanto é 5 * 5',
		'opcoes' : ['25', '55', '10', '51'],
		'resposta' : '25',
	},
	{
		'pergunta' : 'Quanto é 10 / 2',
		'opcoes' : ['4', '5', '2', '1'],
		'resposta' : '5',
	},
]

# Solução
qtd_acertos = 0

for pergunta in perguntas:
	print('Pergunta: ', pergunta['pergunta'])
	print()

	opcoes = pergunta['opcoes']

	for i, opcao in enumerate(opcoes):
		print(f'{i}) Opção: {opcao}')
	
	print()
	
	escolha = input('Escola uma opção: ')

	acertou = False
	escolha_int = None
	qtd_opcoes = len(opcoes)

	if escolha.isdigit():
		escolha_int = int(escolha)

	if escolha_int is not None:
		if escolha_int >= 0 and escolha_int < qtd_opcoes:
			if opcoes[escolha_int] == pergunta['resposta']:
				acertou = True

	print()
	if acertou:
		qtd_acertos += 1
		print('Acertou! O')
	else:
		print('Errou! X')


print(f'Print você acertou {qtd_acertos} de {len(perguntas)}, das perguntas.')
