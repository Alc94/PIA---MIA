import pandas as pd

# Usar la función mask para modificar los valores que cumplan una condición
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# mask es lo contrario de where: reemplaza los valores donde la condición es True
# Las notas menores que 5 se sustituyen por 5
notas = alumnos['nota'].mask(alumnos['nota'] < 5, 5)
print(notas, '\n')

# Sobre varias columnas numéricas: los valores mayores que 100 pasan a 100
numerico = alumnos.select_dtypes(include='number')
print(numerico.mask(numerico > 100, 100))
