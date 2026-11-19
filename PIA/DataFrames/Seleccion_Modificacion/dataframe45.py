import pandas as pd

# Eliminar una fila de un DataFrame con la función drop
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Eliminar la fila con etiqueta 0
sin_primera_fila = alumnos.drop(0)
print(sin_primera_fila, '\n')

# Eliminar varias filas
varias_filas = alumnos.drop([0, 2, 4])
print(varias_filas, '\n')

# Eliminar filas segun una condicion (usando sus etiquetas)
suspensos = alumnos[alumnos['nota'] < 5].index
sin_suspensos = alumnos.drop(suspensos)
print(sin_suspensos)