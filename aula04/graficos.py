# importando a biblioteca matplotlib e dando alias (plt) ao nome
import matplotlib.pyplot as plt
import pandas as pd

# lendo arquivo de dados csv
df = pd.read_csv('salarios.csv')

# exibindo dados lidos
print('Dados do arquivo CSV:')
print(df)

# criando area de plotagem do grafico
plt.figure(figsize=(8,5))
# definindo os dados que serão exibidos e cor
plt.bar(df['Nome'], df['Salario'], color='skyblue')
# Definindo título do grafico
plt.title('Salario por Pessoa')
# Definindo eixos do gráfico X e Y
plt.xlabel('Nome')
plt.ylabel('Salario')
# Exibindo o gráfico
plt.show()


