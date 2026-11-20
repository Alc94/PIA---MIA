import pandas as pd

# Reemplazar valores de una columna por medio de la función replace
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Reemplazar un valor por otro
alumnos['nombre'] = alumnos['nombre'].replace('Pepe', 'José')
print(alumnos, '\n')

# Reemplazar varios valores a la vez con un diccionario {antiguo: nuevo}
alumnos['nombre'] = alumnos['nombre'].replace({'Jorge': 'Jorge Luis', 'Aria': 'Ariadna'})
print(alumnos, '\n')

# Reemplazar una lista de valores por uno solo
alumnos['edad'] = alumnos['edad'].replace([22, 24], 23)
print(alumnos)
