import pandas as pd

# Crear un objeto DataFrame a partir de objetos Series

# Objetos Series
nombres = pd.Series(['Ana', 'Luis', 'Marta', 'Pedro'], name = 'nombre')
edades = pd.Series([20, 22, 21, 23], name = 'edad')
notas = pd.Series([8.5, 6.0, 9.2, 7.4], name = 'nota')

# Diccionario de Series
dataframe = pd.DataFrame({'nombre': nombres, 'edad': edades, 'nota': notas})
print(dataframe)

# metodo .concat, usando el name de cada Series como cabecera de columna
dataframe2 = pd.concat([nombres, edades, notas], axis = 1)
print()
print(dataframe2)