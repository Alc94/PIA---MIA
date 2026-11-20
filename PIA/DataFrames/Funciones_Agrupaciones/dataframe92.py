import pandas as pd

# Usar operadores relacionales para comparar elementos de objetos DataFrame
alumnos = pd.read_csv('../datos/alumnos.csv')
numerico = alumnos.select_dtypes(include='number')

# Comparar con un valor
print(numerico > 50, '\n')

# Comparar con otro DataFrame del mismo tamaño y etiquetas
otro = numerico + 1
print(numerico < otro, '\n')
print(numerico == otro, '\n')

# Equivalentes con funciones: eq, ne, lt, le, gt, ge
print(numerico.gt(50), '\n')
print(numerico.eq(otro))
