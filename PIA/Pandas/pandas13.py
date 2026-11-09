import pandas as pd

# Obtener la desviación estándar y el promedio de un conjunto de datos de una serie
serie = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 3])

print("Media:", serie.mean())
print("Desviación estándar:", serie.std())
