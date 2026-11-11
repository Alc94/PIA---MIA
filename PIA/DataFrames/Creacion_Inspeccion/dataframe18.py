import pandas as pd

# Obtener los datos de una columna como una lista Python con tolist
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos)

nombres = alumnos['nombre'].tolist()
print(nombres)
print(type(nombres))