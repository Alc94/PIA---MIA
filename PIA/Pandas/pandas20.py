import numpy as np
import pandas as pd

# Eliminar los valores NaN de una serie con el método dropna
serie = pd.Series([1, np.nan, 3, np.nan, 5])

sinNan = serie.dropna()
print(sinNan)
