import pandas as pd

# Usar las funciones all y any sobre un objeto DataFrame
alumnos = pd.read_csv('../datos/alumnos.csv')
numerico = alumnos.select_dtypes(include='number')
print(alumnos, '\n')

# all: True si TODOS los elementos cumplen la condición
print((numerico > 0).all(), '\n')

# any: True si AL MENOS UN elemento cumple la condición
print((numerico > 100).any(), '\n')

# Por filas (axis=1)
print((numerico > 100).any(axis=1), '\n')

# Sobre toda la tabla, un único resultado
print((numerico > 0).all().all())
print((alumnos['nota'] >= 5).all())
