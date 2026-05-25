'''
Everybody wants to rule the world - Tears of Fears
Exercício - Lista de Tarefas com desfazer e refazer
Música para codar =)
todo = [] -> lista de tarefas
todo = ['fazer café', 'caminhar'] -> Adicionar fazer café
todo = ['fazer café', 'carminhar'] -> Adicionar caminhar
defazer = ['fazer café',] -> Refazer ['caminhar']
defazer = [] -> Refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar']
'''
import os
import json

def listar_tarefas(tarefas):
	print()
	if not tarefas:
		print('Nenhuma tarefa para listar.')
		return # Para a execução

	print('Tarefas:')
	for tarefas in tarefas:
		print(f'\t{tarefa}')

def desfazer(tarefas, tarefas_refazer):
	print()
	if not tarefas:
		print('Nenhuma tarefa para desfazer.')
		return # Para a execução

	# print('Tarefas:')
	# for tarefas in tarefas:
	# 	print(f'\t{tarefa}')

	tarefa = tarefas.pop()
	print(f'{tarefa = } removida da lista.')
	tarefas_refazer.append(tarefa)
	listar_tarefas(tarefas)

def refazer(tarefas, tarefas_refazer):
	print()
	if not tarefas_refazer:
		print('Nenhuma tarefa para refazer.')
		return # Para a execução

	# print('Tarefas:')
	# for tarefas in tarefas:
	# 	print(f'\t{tarefa}')

	tarefa = tarefas_refazer.pop()
	tarefas.append(tarefa)
	listar_tarefas(tarefas)

def adicionar(tarefa, tarefas):
	print()
	tarefa = tarefa.strip()

	if not tarefa:
		print('Você não digitou uma tarefa.')
		return # Para a execução

	# print('Tarefas:')
	# for tarefas in tarefas:
	# 	print(f'\t{tarefa}')

	print(f'{tarefa = } adicionada da lista.')
	tarefas.append(tarefa)
	listar_tarefas(tarefas)


def ler(tarefas, caminho_arquivo):
	dados = []
	try:
		with open(caminho_arquivo, 'r', encoding = 'utf8') as arquivo:
			dados = json.load(arquivo)
	except FileNotFoundError:
		print('Não existe o arquivo ainda')
		salvar(tarefas, caminho_arquivo)
	return dados		


def salvar(tarefas, caminho_arquivo):
	dados = tarefas
	with open(caminho_arquivo, 'w', encoding = 'utf8') as arquivo:
			dados = json.dump(tarefas, arquivo, indent = 2, ensure_ascii = False)
	return dados


CAMINHO_ARQUIVO = 'aula119.json'

tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []


while True:
	print('Comandos: listar, desfazer e refazer')
	tarefa = input('Digite uma tarefa ou comando: ')


	comandos = {
		'listar': lambda: listar_tarefas(tarefas),
		'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
		'refazer': lambda: refazer(tarefas, tarefas_refazer),
		'clear': lambda: os.system('clear'),
		'adicionar': lambda: adicionar(tarefa, tarefas),
	}

	comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
		comandos['adicionar']

	comando()
	salvar(tarefas, CAMINHO_ARQUIVO)

	# if tarefa == 'listar':
	# 	listar_tarefas(tarefas)
	# 	continue
	# elif tarefa == 'desfazer':
	# 	desfazer(tarefas, tarefas_refazer)
	# 	listar_tarefas(tarefas)
	# 	continue
	# elif tarefa == 'refazer':
	# 	refazer(tarefas, tarefas_refazer)
	# 	listar_tarefas(tarefas)
	# 	continue
	# elif tarefa == 'clear':
	# 	os.system('clear')
	# 	continue
	# else:
	# 	adicionar(tarefa, tarefas)
	# 	listar_tarefas(tarefas)
