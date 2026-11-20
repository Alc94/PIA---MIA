import pandas as pd

# Calcular el promedio y la mediana por cada fila y columna con mean y median
alumnos = pd.read_csv('../datos/alumnos.csv')
numerico = alumnos.select_dtypes(include='number')
print(numerico, '\n')

# Por columnas
print(numerico.mean(), '\n')
print(numerico.median(), '\n')

# Por filas
print(numerico.mean(axis=1), '\n')
print(numerico.median(axis=1))
