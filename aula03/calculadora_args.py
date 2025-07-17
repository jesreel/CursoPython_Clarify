# Calculadora com múltiplos argumentos

class Calculadora():
    def somar(self, *args): # '*': tudos 'args': convenção para argumento, poderia ser qualquer variavel
        return sum(args)
        

# criar o objeto da classe Calculadora
calc = Calculadora()

# passagem do argumentos (quantos desejar)
print(calc.somar(2,6)) # retorna 8
print(calc.somar(1,2,3,4,5)) # retorna 15
