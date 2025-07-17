'''
Exercício
Jogo de Avivinhação

- Sistema gera um numero aleatório
- Tem um número de tentativa definido
- Usuario informa um numero dentro do intervalo definido
- Se ele acertou encerra o jogo, se errou, informa se numero é maior ou menor e gera outra tentativa até terminar.

Usa bibliotaca ramdom

# importa a biblioteca ramdom inteira do python (as rd é um alias)
import random as rd

# Traz somente a função randonint da biblioteca random
from random import randint
'''

from random import randint

print('------ Iniciando o Jogo de Adivinhação ------')

# randint() gera numeros inteiros aleatorios no intervalo
numero = randint(0,100)

# numero de tentativas
chances = 10

# numero informado pelo usuário
chute = 0

while chute != numero:
    chute = input('Chute um número de 1 a 100: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1

        if chute == numero:
            print('----------------------------')
            print('Parabén, você acertou o número: {} e você ainda tinha {} chances!'.format(numero, chances))
            print('----------------------------')
            break

        else:
            print('------')
            if chute > numero:
                print('Você errou. Dica: é um número menor!')
            else:
                print('Você errou. Dica: é um número maior!')
            
            print('Você ainda tem {} chances.'.format(chances))
            print('------')

        if chances == 0:
            print('------')
            print('GAME OVER')
            print('Suas chances acabaram, você perdeu!')
            print('------')
            break

    else:
        print('------')
        print('Informação Inválida!')
        print('------') 