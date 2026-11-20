import pandas as pd

# Cambiar el orden de las filas de forma aleatoria con la función sample
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# frac=1 devuelve todas las filas en orden aleatorio
print(alumnos.sample(frac=1), '\n')

# random_state fija la semilla para obtener siempre el mismo orden
# reset_index(drop=True) renumera el índice
print(alumnos.sample(frac=1, random_state=42).reset_index(drop=True), '\n')

# También se puede pedir un número concreto de filas
print(alumnos.sample(n=3, random_state=1))
