import pandas as pd

# Combinar dos objetos DataFrame con la función concat
alumnos = pd.read_csv('../datos/alumnos.csv')

nuevos = pd.DataFrame({
    'nombre': ['Marta', 'Pablo'],
    'edad': [21, 31],
    'peso': [58, 86],
    'altura': [168, 172],
    'nota': [9.0, 5.7]
})

# Unir por filas (axis=0, por defecto); ignore_index renumera el índice
combinado = pd.concat([alumnos, nuevos], ignore_index=True)
print(combinado, '\n')

# Unir por columnas (axis=1)
extra = pd.DataFrame({'curso': ['DAW', 'DAM', 'DAW', 'DAM', 'DAW']})
print(pd.concat([alumnos, extra], axis=1))
