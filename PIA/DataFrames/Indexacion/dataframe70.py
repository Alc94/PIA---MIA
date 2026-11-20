import pandas as pd

# Reiniciar un índice numérico después de eliminar algunos registros con reset_index
alumnos = pd.read_csv('../datos/alumnos.csv')

# Al eliminar filas, el índice queda con huecos
sin_filas = alumnos.drop([1, 3])
print(sin_filas, '\n')

# reset_index crea un índice nuevo, pero guarda el antiguo como columna 'index'
print(sin_filas.reset_index(), '\n')

# drop=True descarta el índice antiguo
print(sin_filas.reset_index(drop=True))
