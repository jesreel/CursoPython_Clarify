'''
Exercício
Calculadora Básica

- Exibe opção das operações básicas ao usuário (+, -, *, /) para que ele informa com qual quer calcular ou da opção de sair
- Usuário informa 2 números e é executada a operação escolhida com base nesses números
- Exibe opção de sair da calculadora ou fazer outra operação, para o usuário escolher
'''

# Calculadora Básica em Python

# Função que exibe a introdução
def intro():
  return '''
  _          _              _   _   _       
 /   /\  |  /  | | |   /\  | \ / \ |_)  /\  
 \_ /--\ |_ \_ |_| |_ /--\ |_/ \_/ | \ /--\ 
                                       
'''

# Função que exibe o menu
def mostrar_menu():
    return '''
        [1] ou [+] para Soma
        [2] ou [-] para Subtração
        [3] ou [*] para Multiplicação
        [4] ou [/] para Divisão
        [5] ou [sair] para encerrar
    '''

# Função que lê os valores
def ler_valores():
    valor01 = int(input('Informe o primeiro valor: '))
    valor02 = int(input('Informe o segundo valor: '))
    return valor01, valor02


# Função de SOMA
def somar(a, b):
   return a + b

# Função de SUBTRAÇÃO
def subtrair(a, b):
   return a - b

# Função de MULTIPLICAÇÃO
def multiplicar(a, b):
   return a * b

# Função de DIVISÃO
def dividir(a, b):
   return a / b


# Função para permanecer ou sair do programa
def continuar_calculadora():
    print('''
        [1] Continuar Calculadora
        [2] Sair da Calculadora
    ''')

    opcao = input('[Continuar] ou [Sair] da Calculadora? ')

    return opcao != '2'


print(intro())
executar = True

# loop principal
while executar:
    print(mostrar_menu())
    operador = input('Informe a opção: ').strip().lower() #strip tira espaço e lower deixa em minuscuo

    if operador in ['5','sair']:
        print('Fechando a Calculadora . . . ')
        break
   
    valor01, valor02 = ler_valores()

    if operador in ['1', '+']:
        resultado = somar(valor01, valor02)

    elif operador in ['2', '-'] :
        resultado = subtrair(valor01, valor02)

    elif operador in ['3', '*'] :
        resultado = multiplicar(valor01, valor02)

    elif operador in ['4', '/'] :
        resultado = dividir(valor01, valor02)
    
    else:
        print('Opção inválida!')
        continue # volta a exeucção do while e não interrompe
    
    
    print('O resultado é: ' + str(resultado))

    executar = continuar_calculadora()

 
#
#print(mostrar_menu())