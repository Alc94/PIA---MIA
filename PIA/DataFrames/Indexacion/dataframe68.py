import pandas as pd

# Especificar nombres de índices arbitrarios a un objeto DataFrame
alumnos = pd.read_csv('../datos/alumnos.csv')

# Asignando una lista con tantos elementos como filas
alumnos.index = ['a', 'b', 'c', 'd', 'e']
print(alumnos, '\n')

# Dando un nombre al propio índice
alumnos.index.name = 'id'
print(alumnos, '\n')

# Al crear un DataFrame con el parámetro index
df = pd.DataFrame({'numeros': [10, 20, 30]}, index=['uno', 'dos', 'tres'])
print(df, '\n')

# Al leer el CSV, con index_col
print(pd.read_csv('../datos/alumnos.csv', index_col='nombre'))
