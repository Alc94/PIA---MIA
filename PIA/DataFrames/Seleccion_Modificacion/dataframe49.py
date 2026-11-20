import pandas as pd

# Agregar una nueva fila a un DataFrame con notación de slicing
alumnos = pd.read_csv('../datos/alumnos.csv')
print(alumnos, '\n')

nueva = pd.DataFrame([['Marta', 21, 58, 168, 9.0]], columns=alumnos.columns)

# Insertar la fila en la posición 2: se corta el DataFrame con slicing y se une
alumnos = pd.concat([alumnos[:2], nueva, alumnos[2:]], ignore_index=True)
print(alumnos, '\n')

# Con iloc el resultado es el mismo
nueva2 = pd.DataFrame([['Sara', 25, 62, 171, 7.0]], columns=alumnos.columns)
alumnos = pd.concat([alumnos.iloc[:1], nueva2, alumnos.iloc[1:]], ignore_index=True)
print(alumnos)
