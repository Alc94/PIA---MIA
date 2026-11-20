import pandas as pd

# Calcular el módulo sobre cada elemento de un objeto DataFrame numérico (una matriz)
alumnos = pd.read_csv('../datos/alumnos.csv')
numerico = alumnos.select_dtypes(include='number')
print(numerico, '\n')

# Resto de dividir cada elemento entre 2 (con el operador %)
print(numerico % 2, '\n')

# Equivalente con la función mod
print(numerico.mod(2), '\n')

# Con una matriz pequeña
matriz = pd.DataFrame([[10, 15, 20], [7, 8, 9]])
print(matriz % 4)
