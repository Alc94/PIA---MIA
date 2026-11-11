import pandas as pd

# Obtener los tipos de datos de las columnas de un DataFrame
ejemplo = pd.read_csv('sample-simple.csv')

# Con .dtypes se mostrara el tipo de dato de cada columna del DataFrame
print(ejemplo.dtypes)
