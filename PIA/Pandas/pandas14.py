import pandas as pd

# Calcular los valores mínimo y máximo de un objeto Series
serie = pd.Series([7, 3, 15, 1, 9])

print("Mínimo:", serie.min())
print("Máximo:", serie.max())
