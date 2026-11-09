import pandas as pd

# Usar la función de agregación agg en un objeto Series.
serie = pd.Series([3, 7, 1, 9, 5])

# agg aplica una o varias funciones de agregación
print(serie.agg("sum"))
print(serie.agg(["min", "max", "mean", "sum"]))
