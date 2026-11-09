import pandas as pd

# Obtener los elementos pares e impares de un objeto Series numérico
serie = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

pares = serie[serie % 2 == 0]
impares = serie[serie % 2 != 0]
print("Pares:\n", pares)
print("Impares:\n", impares)
