import pandas as pd

# Ordenar los registros de un DataFrame por múltiples columnas
alumnos = pd.read_csv('../datos/alumnos.csv')

# Añadimos una columna con valores repetidos para que haya empates
alumnos['curso'] = ['DAW', 'DAM', 'DAW', 'DAM', 'DAW']
print(alumnos, '\n')

# Primero por curso y, dentro de cada curso, por nota
print(alumnos.sort_values(by=['curso', 'nota']), '\n')

# Un orden distinto para cada columna: curso ascendente y nota descendente
print(alumnos.sort_values(by=['curso', 'nota'], ascending=[True, False]))
