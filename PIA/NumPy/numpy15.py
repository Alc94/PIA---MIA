import numpy as np

# Transforma el siguiente array en 8 bits sin signo y muestra cuánto ocupa en memoria
a = np.array([1, -2, 3])
a_u8 = a.astype(np.uint8)
print(a_u8, a_u8.nbytes)

# Transforma el siguiente array en 8 bits sin signo y muestra cuánto ocupa en memoria
b = np.array([1, 254, 255])
b_u8 = b.astype(np.uint8)
print(b_u8, b_u8.nbytes)

# Transforma el siguiente array en 8 bits con signo y muestra cuánto ocupa en memoria
b = np.array([1, 127, 128])
b_i8 = b.astype(np.int8)
print(b_i8, b_i8.nbytes)

# Transforma el siguiente array en 8 bits con signo y muestra cuánto ocupa en memoria
b = np.array([1, -128, -129])
b_i8 = b.astype(np.int8)
print(b_i8, b_i8.nbytes)

# Transforma el siguiente array en float32 y muestra cuánto ocupa en memoria
b = np.array([1, 2, 3])
b_f32 = b.astype(np.float32)
print(b_f32, b_f32.nbytes)

# Transforma el siguiente array en int32 y muestra cuánto ocupa en memoria
b = np.array([1.9, 2.01, 3.51])
b_i32 = b.astype(np.int32)
print(b_i32, b_i32.nbytes)