'''
Consumir API
https://servicodados.ibge.gov.br/api/docs/
'''
import json
import requests

# Consumindo dados da api (requisição por GET)
pesquisa = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/joao")

# Formatando os dados JSON
dados_json = json.loads(pesquisa.text)

print(dados_json[0]['res'][0])
#print(dados_json)

