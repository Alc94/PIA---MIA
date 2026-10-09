# Ordena productos (nombre, precio, stock) por precio y, a igual precio, por nombre.

productos = [
    ("Teclado", 25.0, 10),
    ("Ratón", 15.0, 20),
    ("Monitor", 150.0, 5),
    ("Alfombrilla", 15.0, 50),
    ("Auriculares", 25.0, 15)
    ]

ordenados = sorted(productos, key=lambda p: (p[1], p[0]))

print(f"{"PRODUCTO":<15} {"PRECIO":<12} {"STOCK":<6}")

for nombre, precio, stock in ordenados:
    print(f"{nombre:<15} {precio:<12} {stock:<6}")