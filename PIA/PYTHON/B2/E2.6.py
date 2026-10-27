# Dado un texto, construye {palabra: frecuencia} y devuelve
# las 3 más repetidas usando sorted con key.

texto = input("Introduce un texto: ").lower().split()

frecuencias = {}

for palabra in texto:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    

top3 = sorted(frecuencias.items(), key=lambda item: item[1], reverse=True)[:3]

print('Diccionario: ', frecuencias)

print(top3)

