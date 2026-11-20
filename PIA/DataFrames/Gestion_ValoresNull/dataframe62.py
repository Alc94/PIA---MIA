import numpy as np
import pandas as pd

# Contar los elementos que son nulos (NaN) en un objeto DataFrame
alumnos = pd.read_csv('../datos/alumnos.csv')

# El CSV no tiene nulos, así que los introducimos a mano
alumnos.loc[1, 'nota'] = np.nan
alumnos['peso'] = alumnos['peso'].mask(alumnos['peso'] == 70)
print(alumnos, '\n')

# Nulos por columna
print(alumnos.isna().sum(), '\n')

# Nulos por fila
print(alumnos.isna().sum(axis=1), '\n')

# Total de nulos en todo el DataFrame
print(alumnos.isna().sum().sum())
