import pandas as pd

# Encontrar los elementos que están dentro de un rango
serie = pd.Series([3, 8, 12, 17, 25, 30])

# between incluye ambos extremos por defecto
enRango = serie[serie.between(10, 25)]
print(enRango)