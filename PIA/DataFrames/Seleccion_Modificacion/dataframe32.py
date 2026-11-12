import pandas as pd

# Comprobar si una columna existe en un DataFrame con el operador Python in
alumnos = pd.read_csv('../datos/alumnos.csv')
columna = input('Introduce el nombre de la columna para saber si existe o no: ')

if columna in alumnos.columns:
    print(alumnos[columna])
else:
    print(f'La columna "{columna}" no existe')


print(columna in alumnos.columns)