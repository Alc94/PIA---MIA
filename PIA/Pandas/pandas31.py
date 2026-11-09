import pandas as pd

# Remover los valores duplicados de un objeto Series con drop_duplicates
serie = pd.Series([1, 2, 2, 3, 3, 3, 4])

print(serie.drop_duplicates())
