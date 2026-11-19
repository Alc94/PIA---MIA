import pandas as pd

# Extraer y remover una columna por su nombre a través de la función pop
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos.columns.tolist())

# Extraemos la columna 'nota' y lo quitamos del DataFrame
notas = alumnos.pop('nota')
print(notas)
print(type(notas))

print(alumnos.columns.tolist())

