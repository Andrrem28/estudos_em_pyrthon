# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL
# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
import os

from dotenv import load_dotenv 

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
print(os.getenv('DB_USER'))  # Obtém o valor da variável de ambiente DB_USER
print(os.getenv('DB_PASSWORD'))  # Obtém o valor da variável de ambiente DB_PASSWORD
print(os.getenv('DB_PORT'))  # Obtém o valor da variável de ambiente DB_PORT
print(os.getenv('DB_HOST'))  # Obtém o valor da variável de ambiente DB_HOST