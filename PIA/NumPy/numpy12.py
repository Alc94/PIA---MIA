import numpy as np

a = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
print("Dimesiones del array a: ",a.ndim)
print()

b = np.array([[2, 3], [5, 7], [11, 13], [17, 19], [23, 29], [31, 37]])
print("Dimesiones del array b: ",b.ndim)
print()

c = np.array([[[2, 3], [5, 7]], [[11, 13], [17, 19]], [[23, 29], [31, 37]]])
print("Dimesiones del array c: ",c.ndim)