import pandas as pd

# Obtener el tamaño en bytes del espacio ocupado por los elementos de un objeto Series
serie = pd.Series([1, 2, 3, 4, 5])

# nbytes: bytes ocupados solo por los datos (5 int64 = 40 bytes)
print("nbytes:", serie.nbytes)
# memory_usage incluye también el índice
print("memory_usage en bytes:", serie.memory_usage())
