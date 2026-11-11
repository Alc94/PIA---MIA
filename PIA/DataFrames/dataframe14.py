import pandas as pd

# Cambiar el tipo de dato de una o más columnas con astype
alumnos = pd.read_csv('alumnos.csv')

# Cambiar el tipo de dato de la columna 'Edad' a float64
alumnos['edad'] = alumnos['edad'].astype('float64')

print(alumnos)