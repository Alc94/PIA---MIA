import pandas as pd

# Obtener los primeros y últimos n elementos de un objeto Series
serie = pd.Series(range(1, 21))
n = 3

print("Primeros:\n", serie.head(n))
print("Últimos:\n", serie.tail(n))
