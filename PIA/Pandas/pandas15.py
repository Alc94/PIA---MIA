import pandas as pd

# Obtener estadísticas básicas de un objeto Series con el método describe
serie = pd.Series([4, 8, 15, 16, 23, 42])

# count, mean, std, min, cuartiles y max
print(serie.describe())
