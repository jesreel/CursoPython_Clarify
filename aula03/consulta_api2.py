import json, requests

nome = input('Qual seu nome? ')
localidade = 0

while localidade < 1 or localidade > 2:
    localidade = int(input('Você deseja selecionar uma localidade? \n [1] Sim \n [2] Não \n'))

if localidade == 1:
    uf = input('Qual uf deseja buscar? \n [35] SP \n [33] RJ \n [31] MG \n [43] RS \n [53] DF \n')
    resultado = requests.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}?localidade={uf}")

if localidade == 2:
    resultado = requests.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}")

print('''
      [1] - 1930
      [2] - 1930 até 1940
      [3] - 1940 até 1950
      [4] - 1950 até 1960
      [5] - 1960 até 1970
      [6] - 1970 até 1980
      [7] - 1980 até 1990
      [8] - 1990 até 2000
      [9] - 2000 até 2010
''')

# A contagem precisa ser a partir de 0. Então coloco -1 para que
# o valor sempre seja 1 abaixo do digitado
periodo = int(input('Selecione o período: ')) -1

dados_json = json.loads(resultado.text)

print(dados_json[0]['res'][periodo]['frequencia'])

