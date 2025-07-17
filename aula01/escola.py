# Estruturas de Decisão e Controle (if .. elif .. else)

tipoEscola = int(input("Tipo Escola (1: Pública 2: Privada ): "))
nomeAluno =  input("Nome do Aluno: ")
mediaAluno = float(input("Média do Aluno: "))
frequenciaAluno = float(input("Frequência do Aluno (em %): "))
mediaEscola = 7


'''
!= diferente
== igual
< menor
<= menor ou igual
> maior
>= maior ou igual
'''

# Escola Pública
if tipoEscola == 1: 
    print("------- Escola Pública -------")
    print("Frequência: ", frequenciaAluno)
    print("Média: ", mediaAluno)

    if (mediaAluno >= mediaEscola) or (frequenciaAluno >= 75):
        print("Aprovado!")
    else:
        print("Reprovado!")

# Escola Privada
elif tipoEscola == 2: 
    print("------- Escola Pública -------")
    print("Frequência: ", frequenciaAluno)
    print("Média: ", mediaAluno)

    if (mediaAluno >= mediaEscola) and (frequenciaAluno >= 75):        
        print("Aprovado!")
    else:
        print("Reprovado!")
        
else:
    print("Tipo de Escola Inválido!")





