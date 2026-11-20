import pandas as pd

# Usar groupby para agrupar datos por una columna específica y contar la cantidad de elementos
alumnos = pd.read_csv('../datos/alumnos.csv')

# Añadimos una columna por la que agrupar
alumnos['curso'] = ['DAW', 'DAM', 'DAW', 'DAM', 'DAW']
print(alumnos, '\n')

# Número de filas por grupo
print(alumnos.groupby('curso').size(), '\n')

# Elementos no nulos de cada columna, por grupo
print(alumnos.groupby('curso').count(), '\n')

# Contar solo una columna
print(alumnos.groupby('curso')['nombre'].count())
