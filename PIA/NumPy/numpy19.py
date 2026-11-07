import numpy as np

""" Fija la semilla, de esta forma los numeros aleatorios son siempre los mismos """
np.random.seed(0)

# Ventas diarias simuladas con media 500 y desviación estándar 50
""" Genera 365 valores (uno por dia) """
sales_data = np.random.normal(500, 50, 365)

# Ventas atípicas por promociones
sales_data[[50, 120, 180, 250, 300]] = [1500, 1400, 1600, 1700, 1800]

""" EJERCICIO 1: Detecta y elimina los valores atípicos 
(aquellos que están fuera de 3 desviaciones estándar del promedio)."""

# Calculo de la media con los datos originales
media = sales_data.mean()

# Calculo de la desviacion tipica con los datos originales
desviacion = sales_data.std()

# Se calcula las ventas que cumplan a que esten inferior a 3 desviaciones del promedio
# sales_data - media es la distancia de cada dia a la media
# abs detecta atipicos como altos y bajos
mascara = np.abs(sales_data - media) <= 3 * desviacion

# Filtrado booleano que devuelve una copia con solos los dias validos
limpio = sales_data[mascara]

print("Eliminados:", sales_data.size - limpio.size, "dias")
print("Quedan:", limpio.size, "dias")

""" EJERCICIO 2: Calcula el promedio, la mediana y la desviación estándar
de las ventas después de limpiar los datos. """
media_limpio = limpio.mean()
mediana_limpio = np.median(limpio)
desviacion_limpio = limpio.std()

print("Media o promedio:", media_limpio)
print("Mediana:", mediana_limpio)
print("Desviacion tipica:", desviacion_limpio)


""" EJERCICIO 3: Genera una vista de las ventas de cada trimestre (3 primeros meses, 3 siguientes, etc.) """
# arra_split(limpio, 4) crea una lista con 4 arrays, cada array contiene 90 dias con sus respectivas ventas
trimestres = np.array_split(limpio, 4)

for i, t in enumerate(trimestres, start=1):
    print(f"Trimestre {i}: {t.size} dias, media {round(t.mean(), 2)}")
    
""" EJERCICIO 4: Encuentra los 5 días con las ventas más bajas después de la limpieza de los datos."""
indices = np.argsort(limpio)[:5]
dias_vBajas = limpio[indices]
print(f"5 dias con las ventas mas bajas:", dias_vBajas)