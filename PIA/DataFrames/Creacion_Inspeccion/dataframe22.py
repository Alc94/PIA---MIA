import pandas as pd

# Cambiar el tipo de una columna de float a int con la función astype
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos)

alumnos['nota'] = alumnos['nota'].astype(dtype='int64')
print(alumnos)