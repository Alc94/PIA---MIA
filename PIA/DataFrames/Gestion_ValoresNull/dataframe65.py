import numpy as np
import pandas as pd

# Reemplazar los NaN (nulo) con un valor específico usando la función fillna
alumnos = pd.read_csv('../datos/alumnos.csv')

# El CSV no tiene nulos, así que los introducimos a mano
alumnos.loc[1, 'nota'] = np.nan
alumnos['peso'] = alumnos['peso'].mask(alumnos['peso'] == 70)
print(alumnos, '\n')

# Un mismo valor para todo el DataFrame
print(alumnos.fillna(0), '\n')

# Un valor distinto por columna
print(alumnos.fillna({'nota': 0, 'peso': 60}), '\n')

# Con la media de la columna
alumnos['nota'] = alumnos['nota'].fillna(alumnos['nota'].mean())
print(alumnos, '\n')

# Con el valor de la fila anterior
print(alumnos.ffill())
