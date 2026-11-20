import pandas as pd

# Redondear valores reales con la función DataFrame.round
alumnos = pd.read_csv('../datos/alumnos.csv')

# Columna con muchos decimales
alumnos['imc'] = alumnos['peso'] / (alumnos['altura'] / 100) ** 2
print(alumnos, '\n')

# Redondear todo el DataFrame numérico a 1 decimal
print(alumnos.round(1), '\n')

# Un número de decimales distinto por columna
print(alumnos.round({'imc': 2, 'nota': 0}), '\n')

# Decimales negativos: redondea a decenas
print(alumnos[['peso', 'altura']].round(-1))
