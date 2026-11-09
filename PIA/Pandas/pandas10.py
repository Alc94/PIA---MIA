import pandas as pd

# Agregar datos a un objeto Series existente.
serie = pd.Series([10, 20, 30])

# pd.concat une series (append ya no existe en pandas)
nuevos = pd.Series([40, 50])
""" Sin el parametro ignore_index=True, los valores nuevos se indexan de nuevo como 0 y 1 """
serie = pd.concat([serie, nuevos], ignore_index=True)
print(serie)

# También se puede añadir un elemento asignando un índice nuevo
serie[5] = 60
print(serie)
