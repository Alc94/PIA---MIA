import pandas as pd

# Reemplazar valores que no cumplan una condición a través de la función DataFrame.where
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# where conserva los valores que SÍ cumplen la condición y reemplaza el resto
# Por defecto, el reemplazo es NaN
notas = alumnos['nota'].where(alumnos['nota'] >= 5)
print(notas, '\n')

# Indicando el valor de reemplazo: las notas menores que 5 pasan a ser 5
notas = alumnos['nota'].where(alumnos['nota'] >= 5, 5)
print(notas, '\n')

# Sobre un DataFrame numérico completo
numerico = alumnos.select_dtypes(include='number')
print(numerico.where(numerico >= 50, 0))
