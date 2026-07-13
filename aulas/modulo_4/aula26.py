# requests para requisição HTTP
import requests

url = 'sua_url_configurada_no_servidor'

response = requests.get(url)

print(response)
# print(response.headers)
# print(response.content)