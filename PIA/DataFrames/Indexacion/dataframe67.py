import pandas as pd

# Seleccionar una columna de un DataFrame como índice con set_index
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# La columna 'nombre' pasa a ser el índice (y deja de ser una columna)
por_nombre = alumnos.set_index('nombre')
print(por_nombre, '\n')

# Ahora se puede acceder con loc por el nombre
print(por_nombre.loc['Pepe'], '\n')

# drop=False mantiene la columna además de usarla como índice
print(alumnos.set_index('nombre', drop=False))
