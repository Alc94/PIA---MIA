import pandas as pd

# Ordenar los valores de un objeto Series con el método sort_values.
serie = pd.Series([50, 10, 40, 20, 30])

# Ordenacion ascendente
print(serie.sort_values())

print()

# Ordenacion descendente
print(serie.sort_values(ascending=False))
