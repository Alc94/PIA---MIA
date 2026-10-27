# Normaliza una lista de valores al rango 0-1 con una sola comprensión.

# E2.5 normalización min-max
valores = [12, 7, 30, 18]

lo, hi = min(valores), max(valores)

# Normalizacion: Tecnica de preprocesamiento de datos que transforma los valores de una variable
# numerica para que queden acotados dentro de un rango especifico, entre 0 y 1

# Valor menos por el valor minimo, dividido entre, el valor maximo menos el valor minimo
norm = [round((v - lo) / (hi - lo), 2) for v in valores]
# [0.17, 0.0, 1.0, 0.48]

print(norm)