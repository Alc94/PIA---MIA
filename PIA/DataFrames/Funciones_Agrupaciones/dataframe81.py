import pandas as pd

# Agrupar un conjunto de datos y luego calcular su promedio con groupby y mean
alumnos = pd.read_csv('../datos/alumnos.csv')

# Añadimos una columna por la que agrupar
alumnos['curso'] = ['DAW', 'DAM', 'DAW', 'DAM', 'DAW']
print(alumnos, '\n')

# Promedio de una columna por grupo
print(alumnos.groupby('curso')['nota'].mean(), '\n')

# Promedio de varias columnas por grupo
print(alumnos.groupby('curso')[['edad', 'peso', 'altura', 'nota']].mean(), '\n')

# Promedio de todas las columnas numéricas
print(alumnos.groupby('curso').mean(numeric_only=True))
