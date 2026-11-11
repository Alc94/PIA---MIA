import pandas as pd

# Mostrar un reporte con la información básica de un objeto DataFrame
ejemplo = pd.read_csv('../datos/sample-simple.csv')

# Mientras que con .info() se mostrara una información mas general de las columnas
print(ejemplo.info())