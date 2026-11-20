import pandas as pd

# Calcular el promedio de los valores de una columna de un DataFrame
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Promedio de una columna
print(alumnos['nota'].mean(), '\n')

# Redondeado a 2 decimales
print(round(alumnos['nota'].mean(), 2), '\n')

# Promedio de varias columnas
print(alumnos[['edad', 'nota']].mean(), '\n')

# Promedio de las filas que cumplen una condición
print(alumnos.loc[alumnos['edad'] > 24, 'nota'].mean())
