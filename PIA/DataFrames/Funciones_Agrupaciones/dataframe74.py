import pandas as pd

# Combinar dos DataFrame y dejar en cada columna el valor mínimo de la suma por columna
# combine recorre las columnas de ambos DataFrame y aplica una función a cada pareja
df1 = pd.DataFrame({'A': [0, 0], 'B': [4, 4]})
df2 = pd.DataFrame({'A': [1, 1], 'B': [3, 3]})
print(df1, '\n')
print(df2, '\n')

# En cada columna nos quedamos con la que tenga menor suma
def menor_suma(s1, s2):
    return s1 if s1.sum() < s2.sum() else s2

print(df1.combine(df2, menor_suma), '\n')

# Con las columnas numéricas de alumnos y una copia modificada
alumnos = pd.read_csv('../datos/alumnos.csv')
numerico = alumnos.select_dtypes(include='number')
otro = numerico.copy()
otro['edad'] = otro['edad'] + 10
otro['nota'] = otro['nota'] - 1
print(numerico.combine(otro, menor_suma))
