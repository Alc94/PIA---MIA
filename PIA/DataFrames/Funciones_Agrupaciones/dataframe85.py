import pandas as pd

# Calcular el elemento menor por cada fila y columna con la función min
alumnos = pd.read_csv('../datos/alumnos.csv')
numerico = alumnos.select_dtypes(include='number')
print(numerico, '\n')

# Mínimo de cada columna
print(numerico.min(), '\n')

# Mínimo de cada fila
print(numerico.min(axis=1), '\n')

# Etiqueta de la fila donde está el mínimo de cada columna
print(numerico.idxmin())
