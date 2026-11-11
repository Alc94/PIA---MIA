import pandas as pd

# Renombrar las columnas de un objeto DataFrame
ejemplo = pd.read_csv('../datos/sample-simple.csv')

nom_columnas = ejemplo.columns.to_list()
print(nom_columnas)
print()

# Para renombrar las columnas debemos nombrar
# la misma cantidad de columnas que se tenga
ejemplo.columns = ['Identificador',
                   'Nombre',
                   'Apellidos',
                   'Correo',
                   'Edad',
                   'Ciudad',
                   'Salario',
                   'Creado'
                   ]

print(ejemplo.columns.to_list())