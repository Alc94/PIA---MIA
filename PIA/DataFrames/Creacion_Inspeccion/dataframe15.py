import pandas as pd

# Obtener la dimensión, el tamaño, y la forma de un objeto DataFrame
alumnos = pd.read_csv('../datos/alumnos.csv')

# Con .shape obtenemos las dimensiones de filas y columnas del DataFrame
print("Numero de filas y columnas:", alumnos.shape)

# Con .size obtenemos el tamaño, es decir, el numero total de elementos
print("Numero total de elementos:", alumnos.size)

# Con .ndim obtenemos la dimension del DataFrame, que siempre sera 2
print("Dimension del DataFrame:", alumnos.ndim)