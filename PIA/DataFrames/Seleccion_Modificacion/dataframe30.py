import pandas as pd

# Seleccionar todas las columnas de un DataFrame, excepto una en particular
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos)

# Con .drop y el nombre de la columna, obtenemos todas las columnas menos la mencionada
columns = alumnos.drop(columns='altura')
print(columns)

# Mediante una condicion con .loc[]
sin_notas = alumnos.loc[:, alumnos.columns != 'nota']
print(sin_notas)

# Mediante una list comprehension
sin_nombres = alumnos[[c for c in alumnos.columns if c != 'nombre']]
print(sin_nombres)