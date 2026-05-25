# Módulos padrão do Python (import, from, as e *)
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# print(sys.platform)

# partes - from nome_modulo import obj1, obj2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform

# print(platform)
# print(exit())

# alias 1 - import nome_modulo as apelido
# alias 2 - from nome_modeulo import objeto as apelido
# Vantagens: você pode reservar nomes para o seu código
# Desvantagens: pode ficar fora do padrão da linguagem
# import sys as s
# sys = 'alguma coisa'
# print(s.platform)
# print(sys)

# from sys import platform as pt
# from sys import exit as ex
# print(pt)
# print(ex())

# má prática: from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import *

# print(platform)
# exit()
