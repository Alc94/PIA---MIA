import pandas as pd

# Obtener como una lista Python los nombres de las columnas de un DataFrame
ejemplo = pd.read_csv('../datos/sample-simple.csv')

# Con .columns obtenemos los nombres de las columnas
# Y con .to_list() lo convertimos en una lista de Python
nom_columnas = ejemplo.columns.to_list()
print(nom_columnas)