import pandas as pd

# Convertir un objeto Series con múltiples listas en un único objeto Series.
lista = [["Colombia", "Perú", "Argentina"], ["Bolivia", "Uruguay"], ["Chile"]]
serie = pd.Series(lista)
print(serie)
print()

# explode() crea una fila por cada elemento de cada lista
# reset_index(drop=True) renumera el índice de 0 a 5
serieUnica = serie.explode().reset_index(drop=True)
print(serieUnica)
