import pandas as pd

# Crea un objeto Series a partir de un filtro aplicado a otro objeto Series.
serie = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# La máscara booleana se usa dentro de los corchetes
mayoresQue5 = serie[serie > 5]
print(mayoresQue5)
