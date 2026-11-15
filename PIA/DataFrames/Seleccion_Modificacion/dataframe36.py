import pandas as pd

# Seleccionar filas y columnas a partir de sus nombres con loc
alumnos = pd.read_csv('../datos/alumnos.csv')


# Un valor concreto: fila con etiqueta 0, columna 'nombre'
print(alumnos.loc[0, 'nombre'])

# varias filas y varias columnas, con listas de etiquetas
print(alumnos.loc[[0, 2, 4], ['nombre', 'nota']])

# Con slicing: el final SI se incluye. Filas 1, 2 y 3
print(alumnos.loc[1:3, 'nombre':'altura'])

# Todas las filas, columnas concretas
print(alumnos.loc[:, ['nombre', 'peso']])
