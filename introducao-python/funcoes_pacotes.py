'''
Funções: códigos que são reutilizáveis e que resolvem uma tarefa específica. Podemos chamar a função várias vezes ao invés de reescrever o mesmo código. 
help(nome_função): retorna explicação do Python sobre determinada função.
'''

# funções
'''
Use print() em combinação com type() para imprimir o tipo de var1.
Use len() para obter o tamanho da lista var1. Envolva-o em uma chamada print() para imprimi-lo diretamente.
Use int() para converter var2 em um inteiro. Armazene a saída como out2.
'''

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)

'''
Use + para combinar o conteúdo de first e second em uma nova lista: full.
Chame sorted() com full e especifique o argumento reverse como sendo True. Salve a lista ordenada como full_sorted.
Para finalizar, imprima full_sorted.
'''

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

# métodos
'''
funções que pertecem a objetos
tudo é um objeto
podemos objetos com métodos associados, dependendo do tipo. dependendo do objeto, o método realiza operações diferentes
'''

'''
Use o método .upper() com place e armazene o resultado em place_up. Use a sintaxe para chamar métodos que você aprendeu no vídeo anterior.
Imprima place e place_up. Ambas mudaram?
Imprima o número de letras “o” na variável place chamando .count() com place e passando a letra 'o' como entrada no método. Estamos falando da variável place, não da palavra "place"!
'''
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)


# Print out the number of o's in place
print(place.count("o"))

'''
Use o método .index() para obter o índice do elemento de areas que é igual a 20.0. Imprima esse índice.
Chame .count() com areas para descobrir quantas vezes 9.50 aparece na lista. Novamente, basta imprimir esse número.
'''
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

'''
Use .append() duas vezes para acrescentar o tamanho de poolhouse (anexo à piscina) e garage (garagem): 24.5 e 15.45, respectivamente. Lembre-se de adicioná-los nesta ordem.
Imprima areas.
Use o método .reverse() para inverter a ordem dos elementos de areas.
Imprima areas mais uma vez.
'''

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)

#pacotes
'''
diretório de scripts Python
script = módulo (especificam funções, métodos, tipos)

instalação de pacotes:
!pip -> https://pip.pypa.io/en/stable/installation/
Download get-pip.py
Terminal:
python3 get-pip.py (indicamos que versão do python estamos usando, ex: python3)
pip3 install numpy (ou qualquer outro pacote)

importar pacotes:
import numpy (ou qualquer outro pacote) as np (apelidando o pacote)

importando função especifica
from numpy import array
'''

'''
Importe o pacote math.
Use math.pi para calcular a circunferência do círculo e armazene-a em C.
Use math.pi para calcular a área do círculo e armazene-a em A.
'''

# Import the math package
import math as mt

# Calculate C
C = 2 * 0.43 * mt.pi

# Calculate A
A = mt.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

'''
Realize uma importação seletiva do pacote math importando apenas a função pi.
Use pi para calcular a circunferência do círculo e armazene-a em C.
Use pi para calcular a área do círculo e armazene-a em A.
'''

# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

