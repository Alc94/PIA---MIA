import pandas as pd

# Calcular el elemento mayor por cada fila y columna con la función max
alumnos = pd.read_csv('../datos/alumnos.csv')
numerico = alumnos.select_dtypes(include='number')
print(numerico, '\n')

# Máximo de cada columna
print(numerico.max(), '\n')

# Máximo de cada fila
print(numerico.max(axis=1), '\n')

# Etiqueta de la fila donde está el máximo de cada columna
print(numerico.idxmax())
