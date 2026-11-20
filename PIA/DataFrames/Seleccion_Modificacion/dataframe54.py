import pandas as pd

# Combinar dos objetos DataFrame con la función merge
alumnos = pd.read_csv('../datos/alumnos.csv')

tutores = pd.DataFrame({
    'nombre': ['Jorge', 'Pepe', 'Aria', 'Marta'],
    'tutor': ['Elena', 'Raúl', 'Elena', 'Raúl']
})

# inner (por defecto): solo los nombres presentes en los dos DataFrames
print(pd.merge(alumnos, tutores, on='nombre'), '\n')

# left: todos los de alumnos, con NaN si no tienen tutor
print(pd.merge(alumnos, tutores, on='nombre', how='left'), '\n')

# outer: todos los registros de ambos
print(pd.merge(alumnos, tutores, on='nombre', how='outer'))
