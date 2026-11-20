import pandas as pd

# Convertir los índices de un DataFrame en una columna con la función reset_index
alumnos = pd.read_csv('../datos/alumnos.csv')

# Dejamos 'nombre' como índice
por_nombre = alumnos.set_index('nombre')
print(por_nombre, '\n')

# reset_index devuelve el índice a una columna y crea uno numérico nuevo
print(por_nombre.reset_index(), '\n')

# Con otro nombre para la columna resultante
print(por_nombre.reset_index().rename(columns={'nombre': 'alumno'}))
