import pandas as pd

# Remover los valores que no cumplan una condición en un objeto Series
serie = pd.Series([5, 12, 3, 20, 8, 15])

# Nos quedamos solo con los que cumplen la condición
resultado = serie[serie > 10]
print(resultado)
