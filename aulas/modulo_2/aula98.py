# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O Python conhece a pasta onde o __main__está e as pastas abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes nos caminhos sys.path

# try:
# 	# import sys
# 	# sys.path.append('Caminho/do/modulo') # Este médoto da biblioteca sys, irá importar os modulos personalizados.	

# except ModuleNotFoundError:
# 	...

# import modulo_personalizado

import aula98_m

print('Modulo', __name__)

aula98_m.soma(10, 30)
print(aula98_m.var_modulo)


