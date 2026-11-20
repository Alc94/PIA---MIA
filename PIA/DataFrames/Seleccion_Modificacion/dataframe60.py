import pandas as pd

# Remover las últimas n filas (registros) de un objeto DataFrame usando iloc
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Quitar las 2 últimas filas: nos quedamos desde el principio hasta la penúltima
print(alumnos.iloc[:-2], '\n')

# Con n en una variable (ojo: si n fuera 0, -0 no funcionaría como se espera)
n = 3
print(alumnos.iloc[:-n])
