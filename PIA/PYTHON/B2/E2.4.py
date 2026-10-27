# Frecuencia de palabras de un texto: normaliza, separa y
# cuenta; muestra el top 5.

SIGNOS = ".,:;!?¡¿()\"'"

def contar_palabras(texto: str) -> dict[str, int]:
    limpio = texto. lower()
    for s in SIGNOS:
        limpio = limpio.replace(s, " ") # quitar puntuación

    palabras = limpio.split()
    conteo: dict[str, int]={}
    
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
        
    return conteo

def top5(conteo: dict[str, int]):
    top5 = sorted(conteo.items(), key=lambda item: item[1], reverse=True)[:5]

    for i, (palabra, frec) in enumerate(top5, start=1):
        print(f"{i}{palabra}{frec}")
        

texto = "Hola, me llamo Alejandro Lopez y soy estudiante del máster de Inteligencia Artificial y Big Data"

frecuencia = contar_palabras(texto)
top5(frecuencia)