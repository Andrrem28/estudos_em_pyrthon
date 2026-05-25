# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
	{'nome': 'Luiz', 'nota': 'A'},
	{'nome': 'Leticia', 'nota': 'B'},
	{'nome': 'Fabricio', 'nota': 'A'},
	{'nome': 'Rosemary', 'nota': 'C'},
	{'nome': 'Joana', 'nota': 'D'},
	{'nome': 'João', 'nota': 'B'},
	{'nome': 'Eduardo', 'nota': 'A'},
	{'nome': 'André', 'nota': 'C'},
	{'nome': 'Anderson', 'nota': 'A'},
]

def ordena(aluno):
	return aluno['nota']

alunos_grupados = sorted(alunos, key = ordena)
grupos = groupby(alunos_grupados, key = ordena)


for chave, grupo in alunos_grupados:
	
	print(chave)

	for aluno in grupo:
		print(aluno)


# grupos = groupby(alunos)

# for chave, grupo in grupos:
# 	print(chave)
# 	print(grupo)