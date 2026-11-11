import pandas as pd

# Renombrar una columna de un DataFrame con la función rename.
ejemplo = pd.read_csv('sample-simple.csv')

nom_columnas = ejemplo.columns.to_list()
print(nom_columnas)
print()

# Con el metodo .rename() podemos renombrar las columnas o filas de un DataFrame
# Para ello debemos de nombrar el nombre actual de la columna y el nuevo nombre a modo de diccionario
ejemplo.rename(columns = {
    'id': 'Identificador',
    'first_name': 'Nombre',
    'last_name': 'Apellidos',
    'email': 'Correo',
    'age': 'Edad',
    'city': 'Ciudad',
    'salary': 'Salario',
    'joined': 'Creado'
    })

print(ejemplo)