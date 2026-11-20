import pandas as pd

# Eliminar filas o registros con la función DataFrame.drop
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Eliminar filas por su etiqueta de índice
print(alumnos.drop(index=[0, 1]), '\n')

# Eliminar según una condición (se obtienen las etiquetas de las filas que la cumplen)
suspensos = alumnos[alumnos['nota'] < 5].index
print(alumnos.drop(suspensos), '\n')

# Eliminar la última fila sin conocer su etiqueta
print(alumnos.drop(alumnos.index[-1]))
