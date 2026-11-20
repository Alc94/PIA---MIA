import numpy as np
import pandas as pd

# Remover valores infinitos (-np.inf y np.inf) de un DataFrame con replace
datos = pd.DataFrame({
    'a': [1.0, np.inf, 3.0, 4.0],
    'b': [-np.inf, 5.0, 6.0, np.nan]
})
print(datos, '\n')

# Convertir los infinitos en NaN
sin_inf = datos.replace([np.inf, -np.inf], np.nan)
print(sin_inf, '\n')

# Después se pueden eliminar las filas con NaN...
print(sin_inf.dropna(), '\n')

# ...o rellenarlas
print(sin_inf.fillna(0))
