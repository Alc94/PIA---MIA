import pandas as pd

# Reemplazar por un valor arbitrario los valores
# de una serie que no satisfagan una condición.
serie = pd.Series([5, 12, 3, 20, 8, 15])
print(serie)
print()

# where conserva los valores que cumplen la condición y sustituye el resto
resultado = serie.where(serie > 10, 0)
print(resultado)
