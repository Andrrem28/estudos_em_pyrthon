# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random
import time
# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(0)

random.seed(time.time())  # Inicializa o gerador de números pseudoaleatórios com uma semente fixa

print(random.seed(0))

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
# r_range = random.randrange(1, 10, 2)  # Gera um número aleatório entre 1 e 10 (exclusivo), com passo de 2
# print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
# r_int = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10 (inclusivo)
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
# r_uniform = random.uniform(1, 10)   
# print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
# random.shuffle(nomes)
# nomes = ['André', 'João', 'Maria', 'Ana', 'Carlos']
# r_shuffle = random.shuffle(nomes)
# print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
# novos_nomes = random.sample(nomes, k = 3)

# print(nomes)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
# novos_nomes_repetidos = random.choices(novos_nomes, k = 3)
# print(novos_nomes_repetidos)
#  -> Escolhe elementos do iterável e retorna outro iterável (não repete valores)
# random.choice(Iterável) -> Escolhe um elemento do iterável
# print(random.choice(novos_nomes_repetidos))