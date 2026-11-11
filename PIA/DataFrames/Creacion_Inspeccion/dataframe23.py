import pandas as pd

# Calcular el número de tipos de datos por cada categoría con dtype.value_counts
alumnos = pd.read_csv('../datos/alumnos.csv')

recuento = alumnos.dtypes.value_counts()

print(recuento)