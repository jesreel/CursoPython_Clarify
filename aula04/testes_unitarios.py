# Testes Unitários com Python

# Função soma
def somar(a, b):
    return a + b

# Função subtrair
def subtrair(a, b):
    return a - b

# Função multiplicar
def multiplicar(a, b):
    return a * b

# Função dividir
def dividir(a, b):
    if b == 0:
        raise ValueError('Não é possível dividir por 0')   

    return a / b
