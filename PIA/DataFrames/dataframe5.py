import pandas as pd

# Obtener las ultimas n filas de un objeto DataFrame

ejemplo = pd.read_csv('sample-simple.csv')

# Para obtener n filas ultimas, se utiliza el método head(n)
# En este caso obtendremos las 3 ultimas filas
print(ejemplo.tail(3))
                      