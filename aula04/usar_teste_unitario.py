# modulo unittest permite escrever testes unitários
import unittest

# importar as funções criadas para testar
from testes_unitarios import somar, subtrair, multiplicar, dividir


# criar a classe com os testes unitários das funções de operações
class TesteOperacoes(unittest.TestCase):
    
    # testar a função de soma
    def teste_soma(self):
        # verificar se a soma de 2 + 3 = 5
        self.assertEqual(somar(2,3), 5)

        # verificar se a soma de -1 + 1 = 0
        self.assertEqual(somar(-1,+1), 0)

        # verificar se a soma de -2 + -3 = -5
        self.assertEqual(somar(-2,-3), -5)

    
    # testar a função de subtrair
    def teste_subtracao(self):
        # verificar se a subtração de 2 - 3 = -1
        self.assertEqual(subtrair(2,3), -1)

        # verificar se a subtração de 0 - 0 = 0
        self.assertEqual(subtrair(0,0), 0)

        # verificar se a subtração de -5 - -3 = 8
        self.assertEqual(subtrair(-5,-3), -2)

    
    # testar a função de multiplicar
    def teste_multiplicacao(self):
        # verificar se a multiplicacao de 2 * 3 = 6
        self.assertEqual(multiplicar(2,3), 6)

        # verificar se a multiplicacao de -2 * 3 = -6
        self.assertEqual(multiplicar(-2,3), -6)

        # verificar se a multiplicacao de 8 * -8 = -64
        self.assertEqual(multiplicar(8,-8), -64)
    


    # testar a função de divisão
    def teste_divisao(self):
        # verificar se a divisão de 6 /2 = 3
        self.assertEqual(dividir(6,2), 3)

        # verificar se a divisão de -6 / -2 = -3
        self.assertEqual(dividir(-6,-2), 3)

        # verificar se a divisão de -6 / -2 = -2
        self.assertEqual(dividir(-6,3), -2)

        #
        with self.assertRaises(ValueError):
            dividir(1,0) # apresenta erro no teste pois nao é possivel divisao por 0



if __name__ == '__main__':
    unittest.main() # executa todos os testes definidos na classe

