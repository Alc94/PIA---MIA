import pandas as pd

# Cambiar el orden del índice de un objeto Series
serie = pd.Series([1, 2, 3, 4, 5], index=["A", "B", "C", "D", "E"])
print(serie)

# reindex reordena según el nuevo orden de etiquetas
serie = serie.reindex(["B", "A", "C", "D", "E"])
print(serie)
