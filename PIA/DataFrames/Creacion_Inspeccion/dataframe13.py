import pandas as pd

# Obtener las columnas de un determinado tipo de dato con select_dtypes
alumnos = pd.read_csv('../datos/alumnos.csv')

print(alumnos)

# Columnas que contengan el tipo de dato int64
print(alumnos.select_dtypes('int64'))

# Columnas que contengan el tipo de dato float64
print(alumnos.select_dtypes('float64'))

# Columnas que contengan el tipo de datos String (object)
print(alumnos.select_dtypes('object'))