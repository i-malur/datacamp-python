#numpy
'''
matrizes np são de um único tipo de dado. Matrizes com diversos tipos de dados são matrizes str
matrizes np são um novo tipo, como strings, floats e lists. Ela possui seus métodos.
'''

'''
Importe o pacote numpy como np, para que você possa fazer referência a numpy com np.
Use np.array() para criar uma matriz do numpy a partir de baseball. Chame essa matriz de np_baseball.
Imprima o tipo de np_baseball para conferir se está certo.
'''
# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

'''
Crie uma matriz do numpy a partir de height_in. Chame essa nova matriz de np_height_in.
Imprima np_height_in.
Multiplique np_height_in por 0.0254 para converter todas as medidas de altura de polegadas em metros. Armazene os novos valores em uma nova matriz, np_height_m.
Imprima np_height_m e verifique se a saída faz sentido.
'''

# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)

'''
O numpy é ótimo para fazer aritmética vetorial. No entanto, se você comparar sua funcionalidade com as listas comuns do Python, algumas coisas mudaram.

Em primeiro lugar, as matrizes do numpy não podem conter elementos com tipos diferentes. Em segundo lugar, os operadores aritméticos típicos, como +, -, * e /, têm um significado diferente nas listas comuns do Python e matrizes do numpy.

Algumas linhas de código já foram disponibilizadas para você. Teste-as e escolha a que melhor corresponde a isto:

np.array([True, 1, 2]) + np.array([3, 4, False])
O pacote numpy já foi importado como np.

resposta: np.array([4, 3, 0]) + np.array([0, 2, 2])
True é convertido para 1 e False para 0.
'''

'''
Subdivida np_weight_lb imprimindo o elemento no índice 50.
Imprima uma submatriz de np_height_in que contenha os elementos no índice 100 até o índice 110 , incluindo este último.
'''
import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])



'''
np_matriz.shape -> é um atributo que apresenta quantas linhas e colunas a matriz tem
todos os dados da matriz são do mesmo tipo
'''


'''
Use np.array() para criar uma matriz 2D do numpy a partir de baseball. Chame-a de np_baseball.
Imprima o tipo de np_baseball.
Imprima o atributo shape de np_baseball. Use np_baseball.shape.
'''
import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

'''
Use np.array() para criar uma matriz 2D do numpy a partir de baseball (lista já carregada). Chame-a de np_baseball.
Imprima o atributo shape de np_baseball.
'''
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

'''
Imprima a 50ª linha de np_baseball.
Crie uma nova variável, np_weight_lb, contendo a segunda coluna inteira de np_baseball.
Selecione a altura (primeira coluna) do 124º jogador de beisebol em np_baseball e imprima-a.
'''

import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49, :])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]

# Print out height of 124th player
print(np_baseball[123, 0])

'''
Você conseguiu obter as alterações de altura, peso e idade de todos os jogadores de beisebol. Estão disponíveis como uma matriz 2D do numpy, updated. Some np_baseball e updated e imprima o resultado.
Você deseja converter as unidades de altura e peso para o sistema métrico (metros e quilogramas, respectivamente). Como primeira etapa, crie uma matriz do numpy com três valores: 0.0254, 0.453592 e 1. Chame essa matriz de conversion.
Multiplique np_baseball por conversion e imprima o resultado.
'''

import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)

#estatística básica
'''
Crie uma matriz do numpy chamada np_height_in que seja igual à primeira coluna de np_baseball.
Imprima a média de np_height_in.
Imprima a mediana de np_height_in.
'''

import numpy as np

# Create np_height_in from np_baseball
np_height_in = np.array(np_baseball[:, 0])

# Print out the mean of np_height_in
print(np_height_in.mean())

# Print out the median of np_height_in
print(np.median(np_height_in))

'''
O código para imprimir a altura média já está incluído. Complete o código da altura mediana.
Use np.std() com a primeira coluna de np_baseball para calcular stddev.
Os jogadores grandes tendem a ser mais pesados? Use np.corrcoef() para armazenar em corr a correlação entre a primeira e a segunda colunas de np_baseball.
'''

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))
