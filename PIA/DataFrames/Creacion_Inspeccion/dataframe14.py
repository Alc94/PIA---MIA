import pandas as pd

# Cambiar el tipo de dato de una o más columnas con astype
alumnos = pd.read_csv("../datos/alumnos.csv")

# Cambiar el tipo de dato de la columna 'edad' a float64
alumnos["edad"] = alumnos["edad"].astype("float64")
# Cambiar el tipo de dato de la columna 'peso' float64
alumnos["peso"] = alumnos["peso"].astype("float64")

print(alumnos)
