import pandas as pd

# Seleccionar filas y columnas específicas de un DataFrame con iloc
alumnos = pd.read_csv('../datos/alumnos.csv')

# Un valor en concreto: fila 0, columna 1 (24 es la edad)
print(alumnos.iloc[0, 1])

# Varias filas y varias columnas, listado con posiciones
print(alumnos.iloc[[0, 2, 4], [0, 2]])

# Slicing: filas 1 a 3 y columnas 0 a 1
print(alumnos.iloc[1:4, 0:2])

# Todas las filas, columnas concretas
print(alumnos.iloc[:, [0, -1]])

# Primeras 3 filas, todas las columnas menos la primera
print(alumnos.iloc[:3, 1:])