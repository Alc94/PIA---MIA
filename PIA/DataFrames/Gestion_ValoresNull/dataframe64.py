import numpy as np
import pandas as pd

# Encontrar los datos en un DataFrame que no son nulos (NaN)
alumnos = pd.read_csv('../datos/alumnos.csv')

# El CSV no tiene nulos, así que los introducimos a mano
alumnos.loc[1, 'nota'] = np.nan
alumnos['peso'] = alumnos['peso'].mask(alumnos['peso'] == 70)
print(alumnos, '\n')

# notna devuelve True donde el dato NO es nulo
print(alumnos.notna(), '\n')

# notnull es un alias de notna
print(alumnos.notnull(), '\n')

# Filas con nota informada
print(alumnos[alumnos['nota'].notna()], '\n')

# Cantidad de datos no nulos por columna
print(alumnos.notna().sum())
