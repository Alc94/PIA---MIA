import pandas as pd

# Cambiar el orden de dos columnas de un objeto DataFrame
alumnos1 = pd.read_csv('../datos/alumnos.csv')
print(alumnos1.columns.tolist())
# Si no indicamos todas las columnas, las columnas no nombradas se eliminaran
alumnos1 = alumnos1[['nota', 'peso', 'nombre']]
print(alumnos1)


# En caso que el dataframe contengan muchas columnas, podemos intercambiarla de esta forma
alumnos2 = pd.read_csv('../datos/alumnos.csv')
# Listamos los nombres de las columnas
columns = alumnos2.columns.tolist()
# Asignamos las variables
i, j = columns.index('nombre'), columns.index('edad')
# Reasignamos
columns[i], columns[j] = columns[j], columns[i]
print()
# Y actualizamos el dataframe
alumnos2 = alumnos2[columns]
print(alumnos2)