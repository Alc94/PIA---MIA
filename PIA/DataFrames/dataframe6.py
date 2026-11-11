import pandas as pd

# Obtener los nombres de las filas y las columnas de un DataFrame

ejemplo = pd.read_csv('sample-simple.csv')

# Junto con index obtenemos los nombres de las filas
filas = ejemplo.index
# Y con columns obtenemos los nombres de las columnas
columnas = ejemplo.columns

print("Nombres de las filas:", filas)
print()
print("Nombres de las columnas:", columnas)