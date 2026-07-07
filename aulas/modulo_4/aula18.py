# secrets gera números aleatórios seguros

import secrets
import string as s
from secrets import SystemRandom as Sr

# print(s.ascii_letters)  # Letras maiúsculas e minúsculas
# print(s.digits)  # Dígitos de 0 a 9
# print(s.punctuation)  # Caracteres de pontuação

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=20)))  # Gera uma senha aleatória de 10 caracteres

random = secrets.SystemRandom()  # Cria um gerador de números aleatórios seguro

# print(secrets.randbelow(10))  # Gera um número aleatório entre 0 e 9 (inclusivo)
# print(secrets.choice(['André', 'João', 'Maria', 'Ana', 'Carlos']))  # Escolhe um elemento aleatório da lista

# print(random.seed(0)) # mas com o secrets, ele não tem a função seed, pois é um gerador de números aleatórios seguro, e não pseudoaleatório.

# r_range = random.randrange(1, 10, 2)  # Gera um número aleatório entre 1 e 10 (exclusivo), com passo de 2
# print(r_range)

# r_int = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10 (inclusivo)
# print(r_int)

# r_uniform = random.uniform(1, 10)   
# print(r_uniform)

# nomes = ['André', 'João', 'Maria', 'Ana', 'Carlos']
# r_shuffle = random.shuffle(nomes)
# print(nomes)

# novos_nomes = random.sample(nomes, k = 3)
# print(nomes)
# print(novos_nomes)

# novos_nomes_repetidos = random.choices(novos_nomes, k = 3)
# random.choice(Iterável) -> Escolhe um elemento do iterável
# print(random.choice(novos_nomes_repetidos))