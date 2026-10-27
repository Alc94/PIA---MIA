# Con zip: calcula el acierto entre etiquetas reales y
# predichas, y crea un dict a partir de columnas y valores.

Y_REAL= ["setosa","virginica","setosa","versicolor"]
Y_PREDICHAS= ["setosa","virginica","setosa","setosa"]

aciertos = sum(r == p for r, p in zip(Y_REAL, Y_PREDICHAS))

print(f"Aciertos: {aciertos / len(Y_REAL):.0%}")

columnas = ["real", "predicho"]
valores = [Y_REAL, Y_PREDICHAS]

tabla = dict(zip(columnas, valores))

print(tabla)