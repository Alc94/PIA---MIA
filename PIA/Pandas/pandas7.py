import pandas as pd

# Cambiar el tipo de datos de un objeto Series.
serie = pd.Series(["100", "200", "python", "300.12", "400"])
print(serie)
print()

# to_numeric con errors="coerce" convierte lo que no sea número en NaN
serieNumerica = pd.to_numeric(serie, errors="coerce")
print(serieNumerica)
print()

# astype cambia el tipo directamente
enteros = pd.Series(["1", "2", "3"]).astype(int)
print(enteros)