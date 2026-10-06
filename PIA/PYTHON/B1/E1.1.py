# Ejercicio 1.1 Conversor de unidades: pide grados Celsius y muestra Fahrenheit y Kelvin con 2 decimales

celsius = float(input("Introduce la temperatura en grados Celsius: "))

fahrenheit = round(((celsius * 9)/5) + 32, 2)

kelvin = round(celsius + 273.15, 2)

print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit y {kelvin} grados Kelvin.")