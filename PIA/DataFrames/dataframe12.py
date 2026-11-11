import pandas as pd

# Obtener estadísticas básicas en un objeto DataFrame con la función describe
alumnos = pd.read_csv('alumnos.csv')

print(alumnos)
print(alumnos.describe())