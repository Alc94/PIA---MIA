# Adivina el numero: bucle while con intentos limitads y pistas mayor/menor.

import random

contador = 0
numero = int(input("Introduce un numero para poder adivinarlo. Si no lo adivinas en 5 intentos, se acabara el juego: "))
num = random.randint(1, 100)

while numero != num and contador < 10:

    contador += 1

    if numero < num:
        print("El numero es MAYOR.")
    elif numero > num:
        print("El numero es MENOR.")
    else:
        print("HAS ACERTADO!!!")

    numero = int(input("Otro numero: "))

print(f"El numero era {num}")

