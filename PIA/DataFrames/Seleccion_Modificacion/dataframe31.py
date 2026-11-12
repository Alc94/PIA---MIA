import pandas as pd

# Seleccionar columnas de un objeto DataFrame usando notación de slicing
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos)
print()

# Elegiremos desde la segunda columna y la penultima (edad, peso y altura)
columnas = alumnos.iloc[:, 1:-1]
print(columnas)
# Obtener solamente la primera y ultima columna (nombre, nota)
nombre_nota = alumnos.iloc[:, [0, -1]]
print(nombre_nota)