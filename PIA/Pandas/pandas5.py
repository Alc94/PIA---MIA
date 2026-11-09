import pandas as pd

diccionario = {"a": 100, "b": 200, "c": 300, "d": 400}

# Convertir un diccionario Python en un objeto Series
# Las claves pasan a ser el índice y los valores los datos
serie = pd.Series(diccionario)
print(serie)
