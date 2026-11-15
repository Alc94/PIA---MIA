import pandas as pd

# Insertar una nueva columna en una posición arbitraria con la función insert
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Insertar 'curso' en la posicion 1 (segunda columna)
# Eso conlleva a que la columna 1 en adelante, se posicione en la siguiente columna
alumnos.insert(1, 'curso', '1 DAW')
print(alumnos, '\n')

# Con una lista de valores (debe tener tantos elementos como filas)
alumnos.insert(0, 'id', range(1, len(alumnos) + 1))
print(alumnos, '\n')

# Con una columna calculada a partir de otra
alumnos.insert(len(alumnos.columns), 'aprobado', alumnos['nota'] >= 5)
print(alumnos, '\n')