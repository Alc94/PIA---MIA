# Con map: convierte ["3,5", "2,25", "7"] en floats
# cambiando la coma por punto.

lista_string = ["3,5", "2,25", "7"]

lista_float = list(map(lambda x: float(x.replace(",", ".")), lista_string))

print(lista_float)