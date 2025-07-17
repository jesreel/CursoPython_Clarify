""" Trabalhando com tipificações e variáveis """

nome = "Jesreel"            # string (tipo texto)
sobrenome = 'de Morais'     # string (tipo texto)
idade =  39                 # integer (tipo numero inteiro)
altura = 1.70               # float  (tipo numero flutuante)
bermuda = False             # boolean (tipo booleano True/False)

# Posso exibir texto com integer usando virgula
print("Meu nome é: ", nome + " "+ sobrenome + ". Tenho ", idade, " anos") 

# Posso exibir texto com integer convertendo o tipo
print("Meu nome é: ", nome + " "+ sobrenome + ". Tenho " + str(idade) + " anos") 

# Posso exibir texto com integer usando format
print("Meu nome é {} {}. tenho {} anos.".format(nome, sobrenome, idade))

# Posso exibir texto com integer usando format abreviado (f-string)
print(f"Meu nome é {nome} {sobrenome}. tenho {idade} anos.")


textoVariasLinhas = '''
Esse é um texto de  várias linhas.
Exibir esse texto
'''

print(textoVariasLinhas)