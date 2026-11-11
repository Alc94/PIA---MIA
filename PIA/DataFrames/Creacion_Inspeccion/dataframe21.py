import pandas as pd

# Obtener los tipos de datos de las columnas de un DataFrame con dtypes
alumnos = pd.read_csv("../datos/alumnos.csv")

tipos = alumnos.dtypes

print(tipos)
