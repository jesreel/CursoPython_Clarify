'''
Exercício:
- Perguntar ao usuário qual o ano atual (ou o que ele digitar)
- Perguntar o ano que o usuário nasceu
- verifica o ano digitado e calcular a idade
- mostrar a idade do usuario na tela
- perguntar se quer refazer o teste
    - Se sim - repetir o teste
    - Se não, encerrar o teste
** Deve ser usado função no exercíio
'''

def calcularIdade(anoAtual, anoNascimento):
    idade = int(anoAtual) - int(anoNascimento)
    print('Sua idade é:', idade, 'anos')

teste = True

while teste:
    anoAtual = input('Informe o ano atual: ')
    anoNascimento = input('Informe o ano do seu Nascimento: ')

    calcularIdade(anoAtual, anoNascimento)

    print('\n')

    continuar = input('Deseja refazer o teste (S/N): ')

    if continuar != "S":
        teste = False


# Versão do professor
'''
def calcular_idade():
    anoNsc = int(input('Em que ano vc nasceu? '))
    anoAtl = int(input('Em que ano estamos? '))
    idade = anoAtl - anoNsc
    print('Você tem ' + str(idade) + ' anos')


def perguntar_novamente():
    opcao = input('Deseja testar novamente: Sim ou Não ')
    if opcao.lower() in "sim":
        iniciarprograma()
    else:
        print('Encerrando o programa! Até mais.')
    

def iniciarprograma():
    calcular_idade()
    perguntar_novamente()

# Chamada inicial
iniciarprograma()
'''