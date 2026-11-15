import pandas as pd

# Modificar un valor o entrada específico de un objeto DataFrame usando loc
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Modificar una celda: fila con etiqueta 0, columna 'nota'
alumnos.loc[0, 'nota'] = 10
print(alumnos, '\n')

# Modificar segun una condicion (varias celdas a la vez)
alumnos.loc[alumnos['nombre'] == 'Lucia', 'nota'] = 9.5
print(alumnos, '\n')

# Modificar varias columnas de una fila
alumnos.loc[1, ['nota', 'edad']] = [1, 20]
print(alumnos, '\n')

# Subir un punto a quienes tengan menos de 5
alumnos.loc[alumnos['nota'] < 5, 'nota'] += 1
print(alumnos, '\n')