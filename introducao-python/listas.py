# criação de listas 
'''
Crie uma lista, areas, que contenha a área do corredor (hall), cozinha (kit), sala de estar (liv), quarto (bed) e banheiro (bath), nesta ordem. Use as variáveis predefinidas.
Imprima areas com a função print().
'''
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]
# Print areas
print(areas)

'''
Conclua o código que cria a lista areas. Crie a lista de modo que ela contenha primeiro o nome de cada cômodo como uma string e, em seguida, sua área. Em outras palavras, adicione as strings "hallway", "kitchen" e "bedroom" nos locais apropriados.
Imprima areas novamente; a impressão está mais informativa dessa vez? R. ['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0, 'bedroom', 10.75, 'bathroom', 9.5]
'''

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

'''
Termine a lista de listas para que ela também contenha os dados do quarto (bedroom) e do banheiro (bathroom). Lembre-se de inseri-los em ordem!
Imprima house.
'''

# House information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# subdivisão de listas 

'''
Imprima o segundo elemento da lista areas (ele tem o valor 11.25).
Crie um subconjunto e imprima o último elemento de areas, que é 9.50. Aqui faz sentido usar um índice negativo!
Selecione o número que representa a área da sala de estar (20.0) e imprima-o.
'''

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[____])

# Print out last element from areas
print(areas[____])

# Print out the area of the living room
print(areas[____])

'''
Use o fatiamento para criar uma lista, downstairs, que contém os primeiros 6 elementos de areas.
Crie upstairs como os últimos 4 elementos de areas. Desta vez, simplifique o fatiamento omitindo o índice final (end).
Imprima downstairs e upstairs usando print().
'''

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

'''
Subdivida a lista house para pegar o float 9.5.
'''

house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
print(house[4][1])

# manipulação de listas 

'''
Atualize a área do banheiro para 10.50 metros quadrados em vez de 9.50 usando indexação negativa.
Torne a lista areas mais moderna! Altere "living room" para "chill zone". Não use indexação negativa desta vez.
'''

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50
print(areas)

# Change "living room" to "chill zone"
areas[4] = "chill zone"
print(areas)

'''
Use o operador + para colar a lista ["poolhouse", 24.5] no final da lista areas. Armazene a lista resultante como areas_1.
Amplie ainda mais areas_1 adicionando dados sobre a garagem. Adicione a string "garage" e o float 15.45. Chame a lista resultante de areas_2.
'''

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
print(areas_1)

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]

'''
Apague a string e o float referentes a "poolhouse" na sua lista areas.
Imprima a lista atualizada areas.
'''

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10:12]

# Print the updated list
print(areas)

'''
Altere o segundo comando, que cria a variável areas_copy, de modo que areas_copy seja uma cópia explícita de areas. 
Após a edição, as alterações feitas em areas_copy não devem afetar areas.
'''

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change this command
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
