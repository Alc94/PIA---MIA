import pandas as pd

# Reemplazar valores en un DataFrame con la función replace
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Reemplazar en todo el DataFrame
print(alumnos.replace({'Jorge': 'Jorge Luis', 4.8: 5.0}), '\n')

# Reemplazar solo en una columna concreta: {columna: {antiguo: nuevo}}
print(alumnos.replace({'nota': {4.8: 5.0, 6.0: 6.5}}), '\n')

# Reemplazar una lista de valores por otro
print(alumnos.replace([50, 55], 0), '\n')

# Reemplazar con una expresión regular
print(alumnos.replace(r'^J.*', 'Empieza por J', regex=True))
