import pandas as pd

# Encontrar la cantidad de elementos únicos por cada fila y columna con nunique
alumnos = pd.read_csv('../datos/alumnos.csv')

# Con axis=1 nos referiremos a las filas, ya que por defecto (axis=0)
# se refiere a las columnas
print('Elementos unicos en filas:', alumnos.nunique(axis=1))
print()
print('Elementos unicos en columnas:', alumnos.nunique())