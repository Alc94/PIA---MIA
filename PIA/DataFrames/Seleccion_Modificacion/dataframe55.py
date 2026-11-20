import pandas as pd

# Eliminar registros duplicados de un DataFrame a partir de una columna
alumnos = pd.read_csv('../datos/alumnos.csv')

# Añadimos un registro con un nombre repetido
repetido = pd.DataFrame([['Jorge', 25, 72, 178, 6.5]], columns=alumnos.columns)
alumnos = pd.concat([alumnos, repetido], ignore_index=True)
print(alumnos, '\n')

# Conserva la primera aparición de cada nombre
print(alumnos.drop_duplicates(subset='nombre'), '\n')

# Conserva la última aparición
print(alumnos.drop_duplicates(subset='nombre', keep='last'), '\n')

# Elimina todos los que aparecen más de una vez
print(alumnos.drop_duplicates(subset='nombre', keep=False))
