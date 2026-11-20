import pandas as pd

# Realizar consultas sobre los elementos de un objeto DataFrame con la función query
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Condición simple
print(alumnos.query('nota >= 5'), '\n')

# Varias condiciones
print(alumnos.query('nota >= 5 and edad < 27'), '\n')

# Condición sobre texto
print(alumnos.query('nombre == "Pepe"'), '\n')

# Usando una variable de Python con @
minimo = 7
print(alumnos.query('nota > @minimo'), '\n')

# Pertenencia a una lista
print(alumnos.query('nombre in ["Jorge", "Aria"]'))
