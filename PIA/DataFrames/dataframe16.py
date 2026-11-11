import pandas as pd

# Obtener la cantidad de memoria ocupada por cada columna en un DataFrame
alumnos = pd.read_csv('alumnos.csv')

# Junto con el parametro deep=True, calcula el uso real de memoria
# Con index=False, excluye el indice del resultado, viendo asi solo las columnas
print(alumnos.memory_usage(deep=True, index=False))

# Total en bytes, y en KB
print(alumnos.memory_usage(deep=True).sum())
print(alumnos.memory_usage(deep=True).sum() / 1024)