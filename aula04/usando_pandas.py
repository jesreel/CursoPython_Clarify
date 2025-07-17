# importando a biblioteca pandas e dando alias (pd) ao nome
import pandas as pd 

# criando dataframe com pandas
# dataframe: dados estruturados, como excel, por exemplo
data = {
    'Nome': ['Caio', 'Andressa', 'Emily', 'Davi','Eloara', 'Jesreel', 'Alice'],
    'Idade': [15, 20, 25, 30, 35, 40, 45],
    'Salario': [1000, 2000, 3000, 4000, 5000, 6000, 7000]
}

df = pd.DataFrame(data)

# Exibir o dataframe
print('DataFrame Criado: ')
print(df)

# Exibindo coluna específica do dataframe
print('\n Mostrar a Coluna [Nome]')
print(df['Nome'])

# Filtrar dados do dataframe
print('\n Exibir dados filtrando por pessoas com idade MAIOR que 30')
print(df[df['Idade'] > 30])

# Adicionar nova coluna
df['Imposto'] = df['Salario'] * 0.1
print('\n Dataframe agora com a coluna Imposto')
print(df)

# Média dos salarios
media_salario = df['Salario'].mean()
print('\n Média de salário')
print(media_salario)

# Média dos Impostos
media_imposto = df['Imposto'].mean()
print('\n Média de imposto')
print(media_imposto)

# Salvando dataframe em um arquivo
df.to_csv('salarios.csv', index=False)
df.to_excel('salarios_excel.xlsx', index=False)


# Carregar arquivo externo de dados
df_externo = pd.read_csv('salarios.csv')
print('\n Tabela de dados CSV externa')
print(df_externo)
