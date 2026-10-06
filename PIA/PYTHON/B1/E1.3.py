# Tabla de multiplicar con formato alineado usando f-strings.

numero = int(input("Introduce un numero para mostrar su tabla de multiplicar: "))

print(f"------TABLA DE MULTIPLICAR DEL {numero}------")

for i in range(0, 11):
    res = numero * i
    print(f"{numero} X {i} = {res}")