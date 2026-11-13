import pandas as pd

# Validar con isin si un elemento se halla dentro de un DataFrame
alumnos = pd.read_csv('../datos/alumnos.csv')

# Filtramos por columna y accedemos directamente a cada elemento de la columna referida
# Devuelve Series con True o False
filtro = alumnos['nombre'].isin(['Pepe', 'Jorge'])
# Devuelve solo las filas con True
resultado = alumnos[filtro]
print(resultado)

# De esta forma muestra el DataFrames con True y False
# True donde aparece los elementos elegidos y False lo contrario
print(alumnos.isin(['Pepe', 'Jorge']))

# Con doble .any(), realiza una doble reduccion
# La primera sobre la columna y la segunda sobre el resultado
# Devolviendo solamente un True o False
print(alumnos.isin(['Pepe']).any().any())

# Con un solo .any(), devolveria la columna, con todas sus filas de booleanos
# Y solo aparecia True con la condicion de que existe dicho elemento
print(alumnos.isin([9.2]).any())

# Y para el caso contrario, elementos que NO esten en la lista
# Se niega con ~
print(
    alumnos[~alumnos['nombre'].isin(['Pepe', 'Jorge'])])