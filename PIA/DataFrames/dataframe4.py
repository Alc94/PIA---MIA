import pandas as pd

# Obtener las primeras n filas de un objeto DataFrame

ejemplo = pd.read_csv('sample-simple.csv')

# Para obtener n filas primeras, se utiliza el método head(n)
# En este caso obtendremos las 3 primeras filas
print(ejemplo.head(3))
                      