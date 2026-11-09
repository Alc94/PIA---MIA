import pandas as pd

# Contar los valores repetidos en una serie
serie = pd.Series(["rojo", "azul", "rojo", "verde", "azul", "rojo"])

print(serie.value_counts())
