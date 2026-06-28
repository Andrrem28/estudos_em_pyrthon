# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
# O enum, diferente de um array, ele não inicia na posição 0, mas sim da 1.

import enum

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA  = enum.auto()
    ACIMA    = enum.auto()
    ABAIXO   = enum.auto()

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA']) # A declaração da palavra Direcoes é tratado como uma classe.
# print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA) # Exemplo
# print(Direcoes(1).name, Direcoes['ESQUERDA'].value) # Exemplo

def mover(direcao: Direcoes): # Aplicando a tipagem do tipo Direcoes
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    
    print(f'Movendo para {direcao.name} ({direcao.value})')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)