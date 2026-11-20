import pandas as pd

# Usar la función agg para realizar varias operaciones por un eje de un DataFrame
alumnos = pd.read_csv('../datos/alumnos.csv')
numerico = alumnos.select_dtypes(include='number')

# Varias operaciones sobre todas las columnas
print(numerico.agg(['min', 'max', 'mean']), '\n')

# Una operación distinta para cada columna
print(numerico.agg({'edad': 'mean', 'peso': ['min', 'max'], 'nota': 'median'}), '\n')

# Por filas (axis=1)
print(numerico.agg('sum', axis=1), '\n')

# Con una función propia
print(numerico.agg(lambda col: col.max() - col.min()))
