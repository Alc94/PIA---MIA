import pandas as pd

# Aplicar una función sobre los elementos de un objeto Series
serie = pd.Series([1, 2, 3, 4, 5])

def cuadrado(x):
    return x ** 2

print(serie.apply(cuadrado))

# Funcion flecha (lambda)
print(serie.apply(lambda x: x * 10))
