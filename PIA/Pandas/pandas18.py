import numpy as np
import pandas as pd

# Comprobar si una serie contiene valores NaN
serie = pd.Series([1, 2, np.nan, 4, np.nan])

print(serie.isna())             # True donde hay NaN
print(serie.isna().any())       # ¿Hay algún NaN?
print(serie.isna().sum())       # Cuántos NaN hay