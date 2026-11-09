import numpy as np
import pandas as pd

# Reemplazar los valores NaN (null) de una serie con un valor arbitrario
serie = pd.Series([1, np.nan, 3, np.nan, 5])

print(serie.fillna(0))
