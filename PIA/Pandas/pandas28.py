import pandas as pd

# Convertir el contenido de un objeto Series en formato CSV (Comma Separated Values)
serie = pd.Series([10, 20, 30], index=["a", "b", "c"], name="valores")

# Sin ruta devuelve el texto CSV
print(serie.to_csv())

# Con ruta lo guarda en un fichero
serie.to_csv("serie.csv")
