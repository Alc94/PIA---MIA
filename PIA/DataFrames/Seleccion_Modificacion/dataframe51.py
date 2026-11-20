import pandas as pd

# Iterar cada una de las filas de un DataFrame con la función iterrows
alumnos = pd.read_csv('../datos/alumnos.csv')

# iterrows devuelve en cada vuelta una tupla (índice, Series con la fila)
for indice, fila in alumnos.iterrows():
    print(f"Fila {indice}: {fila['nombre']} tiene {fila['edad']} años y un {fila['nota']} de nota")

# Calcular algo con cada fila
print()
for indice, fila in alumnos.iterrows():
    imc = fila['peso'] / (fila['altura'] / 100) ** 2
    print(f"{fila['nombre']}: IMC = {imc:.2f}")
