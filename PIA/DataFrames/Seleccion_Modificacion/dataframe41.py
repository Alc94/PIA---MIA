import pandas as pd

# Agregar una nueva fila a un objeto DataFrame por medio de loc
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Añadir al final usando como etiqueta el siguiente indice libre
alumnos.loc[len(alumnos)] = ['Juan', 22, 65, 190, 0]
print(alumnos, '\n')

# Variantes:
# Con un diccionario
alumnos.loc[len(alumnos)] = {
    'nombre': 'Beatriz',
    'edad': 19,
    'peso': 50.3,
    'altura': 156,
    'nota': 6.7
}
print(alumnos, '\n')

# Con una Series
alumnos.loc[len(alumnos)] = pd.Series(['Pablo', 31, 86.2, 172, 5.7], index=alumnos.columns)
print(alumnos, '\n')