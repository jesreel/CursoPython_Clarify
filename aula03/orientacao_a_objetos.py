# Introdução Orientação a Objetos

class carro():

    # Cria o objeto
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0  # 0 pra definir o carro parado
    
    # função de acelerar
    def acelerar(self, aceleracao):
        self.velocidade += aceleracao
        print(f'O carro {self.modelo} da cor {self.cor} acelerou {aceleracao} Km/h. Velocidade atual: {self.velocidade} Km/h')

    # função de desacelerar
    def desacelerar(self, aceleracao):
        self.velocidade -= aceleracao
        if self.velocidade > 0:
            print(f'O carro {self.modelo} da cor {self.cor} desacelerou {aceleracao} Km/h. Velocidade atual: {self.velocidade} Km/h')
        else:
            self.parar()
    
    # fução de parar
    def parar(self):
        self.velocidade = 0
        print(f'O carro {self.modelo} da cor {self.cor} parou. Velocidade atual: {self.velocidade} Km/h')



# criar um objeto carro
meu_carro01 = carro('Fusca', 'Amarelo')
meu_carro02 = carro('SJ', 'Preto')

# acelerar o carro 01
meu_carro01.acelerar(20)
meu_carro01.acelerar(20)

meu_carro01.desacelerar(10)
meu_carro01.desacelerar(20)
meu_carro01.desacelerar(10)


# acelerar o carro 02
#meu_carro02.acelerar(30)
#meu_carro02.acelerar(40)

# parar o carro 01
#meu_carro01.parar()

# parar o carro 02
#meu_carro02.parar()

# parar o carro
#meu_carro01.acelerar(20)