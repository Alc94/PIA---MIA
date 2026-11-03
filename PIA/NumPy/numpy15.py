import numpy as np

#Transforma el siguiente array en 8 bits sin signo y muestra cuánto ocupa en memoria
a=np.array([1, -2, 3])
a8bits = a.astype(np.uint8)
print(a8bits.nbytes)

# Transforma el siguiente array en 8 bits sin signo y muestra cuánto ocupa en memoria
b=np.array([1,254,255])


# Transforma el siguiente array en 8 bits con signo y muestra cuánto ocupa en memoria
b=np.array([1,127,128])


#Transforma el siguiente array en 8 bits con signo y muestra cuánto ocupa en memoria
b=np.array([1,-128,-129])

# Transforma el siguiente array en float32 y muestra cuánto ocupa en memoria
b=np.array([1,2,3])


# Transforma el siguiente array en int32 y muestra cuánto ocupa en memoria
b=np.array([1.9,2.01,3.51])

