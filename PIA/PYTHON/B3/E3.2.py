 # E3.2

import csv
from pathlib import Path

RUTA = Path(__file__).parent / "datos" / "iris.csv"

with open(RUTA, newline="") as f:
    filas = list(csv.DictReader(f))

for fila in filas:
    fila["largo_pet"] = float(fila["largo_pet"])
    fila["ancho_pet"] = float(fila["ancho_pet"])
    fila["largo_sep"] = float(fila["largo_sep"])
    fila["ancho_sep"] = float(fila["largo_sep"])

    print()

    print(fila)

cont_setosa = 0
cont_virginica = 0
cont_versicolor = 0
sum_largo_sep, sum_ancho_sep, sum_largo_pet, sum_ancho_pet = 0, 0, 0, 0
media = 0

for fila in filas:
    if fila["clase"] == "setosa":
        cont_setosa += 1

        sum_largo_sep += fila["largo_sep"]
        sum_ancho_sep += fila["ancho_sep"]
        sum_largo_pet += fila["largo_pet"]
        sum_ancho_pet += fila["ancho_pet"]

media_largo_sep = sum_largo_sep / cont_setosa
media_ancho_sep = sum_ancho_sep / cont_setosa
media_largo_pet = sum_largo_pet / cont_setosa
media_ancho_pet = sum_ancho_pet / cont_setosa

print(f"La media de largo del sépalo es: {media_largo_sep:.2f} cm")
print(f"La media de ancho del sépalo es: {media_ancho_sep:.2f} cm")
print(f"La media de largo del pétalo es: {media_largo_pet:.2f} cm")
print(f"La media de ancho del pétalo es: {media_ancho_pet:.2f} cm")