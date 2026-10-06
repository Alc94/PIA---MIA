# Clasificador de notas: pide una nota, valida el rango 0-10 y muestra la calificacion.

nota = float(input("Introduce una nota entre 0 y 10: "))

# VALIDACION DE LA NOTA
while nota < 0 or nota > 10:
    print("Nota no valida. Introduce una nota entre 0 y 10 de nuevo: ")
    nota = float(input())

print(f"Nota válida: {nota}")