import pandas as pd

# Sumar los valores de una columna de un DataFrame con sum
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Suma de una columna
print(alumnos['peso'].sum(), '\n')

# Suma de varias columnas
print(alumnos[['peso', 'altura']].sum(), '\n')

# Suma de las filas que cumplen una condición
print(alumnos.loc[alumnos['nota'] >= 5, 'peso'].sum())
