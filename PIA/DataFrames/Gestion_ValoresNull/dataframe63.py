import numpy as np
import pandas as pd

# Determinar los datos en un DataFrame que son nulos (NaN)
alumnos = pd.read_csv('../datos/alumnos.csv')

# El CSV no tiene nulos, así que los introducimos a mano
alumnos.loc[1, 'nota'] = np.nan
alumnos['peso'] = alumnos['peso'].mask(alumnos['peso'] == 70)
print(alumnos, '\n')

# isna devuelve un DataFrame de booleanos: True donde hay un nulo
print(alumnos.isna(), '\n')

# isnull es un alias de isna
print(alumnos.isnull(), '\n')

# Comprobar si hay algún nulo en cada columna
print(alumnos.isna().any())
