import pandas as pd

# Remover las primeras n filas (registros) de un objeto DataFrame usando iloc
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Quitar las 2 primeras filas: nos quedamos desde la posición 2 hasta el final
print(alumnos.iloc[2:], '\n')

# Con n en una variable
n = 3
print(alumnos.iloc[n:])
