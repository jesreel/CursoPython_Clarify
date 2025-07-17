# calculadora imposto de renda simples

# Função de calcular o IR
def calcular_ir(salario_bruto):

    # tabela do IR (alíquotas e faixas do IR)
    # Tabela exercício 2025 (ano calendário 2024)
    tabela_ir = [
        {"faixa":(0, 2259.20), "aliquota": 0, "deducao":0},
        {"faixa":(2259.21, 2826.65), "aliquota": 7.5, "deducao": 169.44},
        {"faixa":(2826.66, 3751.05), "aliquota": 15, "deducao": 381.44},
        {"faixa":(3751.06, 4664.68), "aliquota": 22.5, "deducao": 662.77},
        {"faixa":(4664.69, float("inf")), "aliquota": 27.5, "deducao": 896.00}        
    ]

    # calcular ir com base na tabela_ir
    imposto = 0

    for faixa in tabela_ir:        
        #calculo do ir para a faixa de salario
        if (salario_bruto > faixa["faixa"][0]) and (salario_bruto <= faixa["faixa"][1]):
            imposto = (salario_bruto * (faixa["aliquota"]/100)) - faixa["deducao"]
            break
    
    return imposto
       

salario_bruto = float(input('Informe seu salário bruto: '))
imposto = calcular_ir(salario_bruto)

print(f'O imposto de renda é de R$ {imposto:.2f}') # :.2f informa que terá 2 casas decimais