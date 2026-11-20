import pandas as pd

# Reemplazar valores de una columna con la función map de un DataFrame
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# map con un diccionario: lo que no esté en el diccionario pasa a NaN
alumnos['nombre_corto'] = alumnos['nombre'].map({'Jorge': 'J', 'Pepe': 'P', 'Aria': 'A'})
print(alumnos, '\n')

# map con una función
alumnos['nota_texto'] = alumnos['nota'].map(lambda n: 'Aprobado' if n >= 5 else 'Suspenso')
print(alumnos, '\n')

# map sobre una Series booleana
print((alumnos['nota'] >= 5).map({True: 'Sí', False: 'No'}))
