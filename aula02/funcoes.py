# Funções em Python

# função SEM VARIÁVEL (parâmetro)
def minhaFuncao():
    print("Olá Mundo!")

# função COM VARIÁVEL (parâmetro)
def MinhaFuncaoMelhorada(animal, idadePet):
    print("Você gosta de:", animal, "e ele tem", idadePet, "anos")


alunos = ['Jesreel', 'Eloara', 'Emily', 'Alice', 'Andressa', 'Davi']
cursos = ['Python', 'PHP', '', 'SQL']


minhaFuncao()
# print(minhaFuncao())

petCliente = input('Qual seu animal preferido: ')
idadePet = input('Qual idade do seu ' + petCliente + ': ') # usar '+' no input ',' nao funciona
MinhaFuncaoMelhorada(petCliente, idadePet)
# print(minhaFuncaoMelhorada(petCliente))

# Chamando a função e passando valores diretamente
MinhaFuncaoMelhorada('Lobo', '10')


