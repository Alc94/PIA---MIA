import pandas as pd

# Ordenar los valores de las columnas de un DataFrame con sort_values
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Orden ascendente por una columna
print(alumnos.sort_values(by='nota'), '\n')

# Orden descendente
print(alumnos.sort_values(by='nota', ascending=False), '\n')

# Ordenar por texto
print(alumnos.sort_values(by='nombre'), '\n')

# Con ignore_index se renumera el índice
print(alumnos.sort_values(by='edad', ignore_index=True))
