import pandas as pd

# Ordenar los índices de un DataFrame con la función sort_index
alumnos = pd.read_csv('../datos/alumnos.csv')

# Desordenamos las filas para ver el efecto
desordenado = alumnos.sample(frac=1, random_state=3)
print(desordenado, '\n')

# Orden ascendente por índice
print(desordenado.sort_index(), '\n')

# Orden descendente
print(desordenado.sort_index(ascending=False), '\n')

# Ordenar las columnas por su nombre (axis=1)
print(alumnos.sort_index(axis=1))
