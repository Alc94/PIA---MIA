import numpy as np
import pandas as pd

# Convertir un arreglo NumPy en un objeto Series
array = np.array([10, 20, 30, 40, 50])

serie = pd.Series(array)
print(array)
print(serie)