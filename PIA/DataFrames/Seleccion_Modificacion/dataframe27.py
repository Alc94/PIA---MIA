import pandas as pd

# Extraer una fila de un DataFrame como un objeto Series
alumnos = pd.read_csv('../datos/alumnos.csv')

primera_fila = alumnos.iloc[0]
print(primera_fila)
print(type(primera_fila))

print()

# En el metodo .loc tambien es valido indicar el indice por numero, como en este caso
# Si los indices tuvieran una etiqueta, se podria acceder tanto por numero como por nombre al indice
primera_fila2 = alumnos.loc[0]
print(primera_fila2)
print(type(primera_fila2))