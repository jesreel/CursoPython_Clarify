# importando a biblioteca numpy e dando alias (np) ao nome
import numpy as np

# criar array numpy (vetor)
array1 = np.array([1,2,3,4,5])

print('Array do numpy')
print(array1)

# operações matemáticas utilizando o array
print('\nArray multiplicado por 2')
print(array1 * 2)

# operações entre 2 arrays diferentes
array2 = np.array([10,20,30,40,50])
print('Soma entre array1 e array2\n')
print(array1 + array2)


# criando matriz 2D
matriz = np.array([[1,2,3], [4,5,6]])
print('\n Matriz 2x3') # matriz 2x3 2 linhas 3 colunas
print(matriz)

# somar elementos da matriz
print('\n Soma de todos os elementos da matriz')
print(np.sum(matriz))

# media dos elementos da matriz
print('\n Média dos elementos da matriz')
print(np.mean(matriz))

# Transposta da matriz 
# Transposta: Girar os elementos da matriz na vertical 
print('\n Matriz transposta')
print(matriz.T)

# Gerar valores aleatorios para matriz
print('\n Numeros aleatorios entre 0 e 1')
print(np.random.rand(3,3)) # gera matriz de 3x3 com valores aleatorios entre 0 e 1

