'''
Calculadora de imposto de renda usando orientação a objetos
Refatoração do código anterior estruturado
'''

class TabelaIR():
    def __init__(self):
        self.tabela = [
        {"faixa":(0, 2259.20), "aliquota": 0, "deducao":0},
        {"faixa":(2259.21, 2826.65), "aliquota": 7.5, "deducao": 169.44},
        {"faixa":(2826.66, 3751.05), "aliquota": 15, "deducao": 381.44},
        {"faixa":(3751.06, 4664.68), "aliquota": 22.5, "deducao": 662.77},
        {"faixa":(4664.69, float("inf")), "aliquota": 27.5, "deducao": 896.00}        
        ]
    
class CalculadoraIR():
    def __init__(self, salario_bruto, tabela_ir):
        self.salario_bruto = salario_bruto
        self.tabela_ir = tabela_ir
    
    def calcular_ir(self):
        imposto = 0
        for faixa in self.tabela_ir.tabela:
            if (self.salario_bruto > faixa["faixa"][0]) and (self.salario_bruto <= faixa["faixa"][1]):
                imposto = (self.salario_bruto * (faixa["aliquota"]/100)) - faixa["deducao"]
                alq = faixa["aliquota"]               
                dd = faixa["deducao"]
                salario_liquido = self.salario_bruto - imposto
                break

        #return imposto
        return [alq, dd, imposto, salario_liquido]


print('========== Calculando Imposto de Renda ==========\n')

salario_bruto = float(input('Informe o salário bruto: '))
tabela_ir = TabelaIR();

calculadora_ir = CalculadoraIR(salario_bruto, tabela_ir)
result = calculadora_ir.calcular_ir()

#print(f'Imposto de renda devido: R$ {imposto:.2f}')
print(f'\n Seu salário bruto: R$ {salario_bruto}  \n Seu salário líquido: R$ {result[3]}  \n Alíquota de IR: {result[0]}%  \n Dedução: R$ {result[1]} \n Imposto de renda devido: R$ {result[2]:.2f}\n')



