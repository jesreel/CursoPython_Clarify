# trabalhando com loopings

palavra = "garrafa"
contador = 1

print("Palavra escolhida: ", palavra)

print("------------------- FOR -----------------")

# loop for (para cada elemento faça)
for letra in palavra:
    print(contador, ': ',letra)
    contador = contador + 1

# lista
cidades = ['Santa Fé do Sul', 'São Paulo', 'São José do Rio Preto', 'Zihuatanejo']

for cidade in cidades:
    print(cidade)
    
print(cidades[2])

print(type(cidades))


print("------------------- While -----------------")

botaoExecutar = True
contador = 0

# loop while (enquanto verdade faça)
while botaoExecutar == True:
    if contador <= 10:
        print(contador)
        contador = contador + 1
    else:
        botaoExecutar = False


'''
Exercício:
- Criar lista de compras
- Exibir na tela os itens da lista
'''

listaDeCompras = ['Sabão', 'Arroz', 'Alho', 'Macarrão', 'Carne', 'Ovo', 'Legumes', 'Verduras']

#Exibindo itens da lista
print("--- Lista de Compras ---")
for item in listaDeCompras:
    print('[x]', item)










