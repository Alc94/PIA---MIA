import pandas as pd

# Elimina los outliers dentro de la lista del ejercicio de ejemplo de Pandas

# Lista de ejemplo con dos valores atípicos (150 y -40)
serie = pd.Series([10, 12, 11, 13, 12, 150, 11, 10, 14, -40, 12])

# Método del rango intercuartílico (IQR)
q1 = serie.quantile(0.25)
q3 = serie.quantile(0.75)
iqr = q3 - q1
limiteInferior = q1 - 1.5 * iqr
limiteSuperior = q3 + 1.5 * iqr

sinOutliers = serie[serie.between(limiteInferior, limiteSuperior)]
print("Límites:", limiteInferior, limiteSuperior)
print(sinOutliers)
