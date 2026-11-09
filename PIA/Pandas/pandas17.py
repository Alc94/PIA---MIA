import pandas as pd

# Extraer los datos de un objeto Series como un objeto NumPy
serie = pd.Series([10, 20, 30, 40])

array = serie.to_numpy()
print(array)
print(type(array))
