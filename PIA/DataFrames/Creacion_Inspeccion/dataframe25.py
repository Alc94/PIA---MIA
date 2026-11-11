import pandas as pd

# Obtener la representación en NumPy de un objeto DataFrame
alumnos = pd.read_csv('../datos/alumnos.csv')

# Se puede realizar de dos formas, tanto con pd.values o pd.to_numpy()
# De esta forma desaparecen los nombres de las columnas y los indices de cada fila
values = alumnos.values
toNumpy = alumnos.to_numpy()

print(values)
print()
print(toNumpy)