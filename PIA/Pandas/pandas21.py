import pandas as pd

# Calcular el valor absoluto de los elementos de un objeto Series
serie = pd.Series([-5, 3, -2, 8, -1])

print(serie.abs())