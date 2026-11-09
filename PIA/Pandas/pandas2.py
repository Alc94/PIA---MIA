import pandas as pd

serie = pd.Series([1, 2, 3, 4, 5])

# Ejercicio 2: Convertir un objeto Series a una lista Python
# tolist() devuelve una lista de Python
lista = serie.tolist()
print(lista)
print(type(lista))
