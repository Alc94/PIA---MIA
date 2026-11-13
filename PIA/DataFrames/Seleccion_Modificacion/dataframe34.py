import pandas as pd

# Obtener registros a partir de sus índices numéricos con iloc
alumnos = pd.read_csv('../datos/alumnos.csv')

# Devuelve una sola fila, siendo un objeto Series
print(alumnos.iloc[0])
print(type(alumnos.iloc[0]))

# Para que devuelva una fila como un objeto DataFrames, se utilizaria doble corchete
print(alumnos.iloc[[0]])
print(type(alumnos.iloc[[0]]))

# Obtener varias filas en concreto
print(alumnos.iloc[[0, 2, 4]])

"""  
Obtener un rango de filas: Filas 1 a la 3, la fila 4 NO se incluye
De esta forma obtenemos un objeto DataFrames por la seleccion multiple de filas.
Sin slicing, Pandas colapsa la tabla y devuelve una Series.
"""
print(alumnos.iloc[1:4])
print(type(alumnos.iloc[1:4]))