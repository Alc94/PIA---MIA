import numpy as np
from sklearn.datasets import load_iris

datos = load_iris().data
resultado = load_iris().target

x = datos[:99, [0, 2]]
y = resultado[:99]

xy = np.column_stack((x, y))

print(xy.shape)
print(xy)