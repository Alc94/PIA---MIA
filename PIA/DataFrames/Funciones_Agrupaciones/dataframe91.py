import pandas as pd

# Calcular la transpuesta de un objeto DataFrame con transpose o T
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

# Con el atributo T
print(alumnos.T, '\n')

# Con el método transpose
print(alumnos.transpose(), '\n')

# Con un índice significativo queda más legible
print(alumnos.set_index('nombre').T)
