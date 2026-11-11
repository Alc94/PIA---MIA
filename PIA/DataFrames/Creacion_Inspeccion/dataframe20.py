import pandas as pd

# Obtener los elementos distintos de una columna de un DataFrame con unique
alumnos = pd.read_csv('../datos/alumnos.csv')

unicos = alumnos['nombre'].unique()
print('Cantidad de nombres unicos:', unicos)