# Detalhando strings e usando formatação

nomeCompleto = "Jesreel de Morais"
inicio = 11
fim = (inicio + 6)

'''
Fatiamento de strings
inicia-se em 0 e o último caractere é exclusivo (precisa adicionar +1)
'''
#print(nomeCompleto[11:17])
#print(nomeCompleto[inicio:fim])


# Criando campos de entrada de texto para usuário digitar

'''nome = input("Escreva seu nome: ")
sobrenome = input("Escreva seu sobrenome: ")

print("Nome Completo: " + nome +' '+ sobrenome)

print(f"Nome: {nome} \nSobrenome: {sobrenome} \nNome Completo: {nome +' '+ sobrenome}") '''


'''
Todo valor digitado em um input retorna uma string.
Para trabalhar com valores numéricos, precisa converter
A conversão pode ser tanto no input como na váriavel que armazena o valor
'''

caixinha01 = int(input("Insira o valor01: "))
caixinha02 = int(input("Insira o valor02: "))

resultado = caixinha01 + caixinha02
# poderia ser feita a conversao na variável--> resultado = int(caixinha01) + int(caixinha02)

print("Resultado: ", resultado)
