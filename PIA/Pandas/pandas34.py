import numpy as np
import pandas as pd

# En una Serie de Pandas donde se registran las ventas mensuales de un producto durante años,
# utiliza el método group by para calcular las ventas medias en cada mes.

# Ventas mensuales durante 3 años (2022-2024)
fechas = pd.date_range("2022-01-01", periods=36, freq="MS")
np.random.seed(0)
ventas = pd.Series(np.random.randint(100, 500, size=36), index=fechas)
print(ventas)

# Agrupamos por el mes del índice y calculamos la media
mediaPorMes = ventas.groupby(ventas.index.month).mean()
print(mediaPorMes)