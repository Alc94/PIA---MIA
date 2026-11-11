import pandas as pd

# Contar el número de columnas que tiene un DataFrame
alumnos = pd.read_csv('../datos/alumnos.csv')

contador_len = len(alumnos.columns)
contador_shape = alumnos.shape[1]

print('Numero de columnas con metodo "len":', contador_len)
print('Numero de columnas con metodo "shape":', contador_shape)