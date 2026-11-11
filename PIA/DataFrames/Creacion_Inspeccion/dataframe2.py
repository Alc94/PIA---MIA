import pandas as pd

# Leer un archivo CSV con la función read_csv para crear un DataFrame

archivo_csv = pd.read_csv('../datos/sample-simple.csv')
print(archivo_csv)