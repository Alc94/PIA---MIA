import numpy as np
import pandas as pd

# Seleccionar los registros que tienen un campo nulo (nan) dentro de una columna
alumnos = pd.read_csv('../datos/alumnos.csv')

# El CSV no tiene nulos, así que los introducimos a mano
alumnos.loc[1, 'nota'] = np.nan
alumnos['peso'] = alumnos['peso'].mask(alumnos['peso'] == 70)
print(alumnos, '\n')

# Filas donde 'nota' es nulo
print(alumnos[alumnos['nota'].isna()], '\n')

# Filas donde 'peso' es nulo
print(alumnos[alumnos['peso'].isnull()], '\n')

# Filas con algún nulo en cualquier columna
print(alumnos[alumnos.isna().any(axis=1)])
