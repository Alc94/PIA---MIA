import pandas as pd

# Eliminar registros que no cumplan con una condición sobre una columna específica
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Nos quedamos solo con los que cumplen la condición
aprobados = alumnos[alumnos['nota'] >= 5]
print(aprobados, '\n')

# Equivalente con loc, renumerando el índice
aprobados = alumnos.loc[alumnos['nota'] >= 5].reset_index(drop=True)
print(aprobados, '\n')

# Equivalente con drop sobre las filas que NO cumplen
sin_suspensos = alumnos.drop(alumnos[alumnos['nota'] < 5].index)
print(sin_suspensos)
