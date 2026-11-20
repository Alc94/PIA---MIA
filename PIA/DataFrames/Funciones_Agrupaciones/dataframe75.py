import pandas as pd

# Aplicar una función a todos los elementos de un DataFrame con la función apply
alumnos = pd.read_csv('../datos/alumnos.csv')
numerico = alumnos.select_dtypes(include='number')

# Sobre una columna: cada elemento pasa por la función
print(alumnos['nota'].apply(lambda n: 'Aprobado' if n >= 5 else 'Suspenso'), '\n')

# Sobre el DataFrame, por columnas (axis=0): la función recibe cada columna
print(numerico.apply(lambda col: col.max() - col.min()), '\n')

# Por filas (axis=1): la función recibe cada fila
alumnos['imc'] = alumnos.apply(lambda fila: fila['peso'] / (fila['altura'] / 100) ** 2, axis=1)
print(alumnos)
