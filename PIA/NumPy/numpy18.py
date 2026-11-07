import numpy as np

datos = np.loadtxt("wine.csv", delimiter=",")
print(datos.shape)

def imprimir_datos(matriz):
    
    # Apartado 1: Mostrar cuantas caracteristicas hay de cada tipo de vino
    # Todas las columnas menos la ultima, que indica el tipo de vino
    num_caracteristicas = matriz.shape[1] - 1
    print("Numeros de caracteristicas:", num_caracteristicas)
    
    # Apartado 2: Mostrar cuantas filas hay
    print("Numero de filas que contiene la matriz:",matriz.shape[0])
    
    # Apartado 3: Mostrar cuantos tipos de vino tenemos y cuales son
    tipos = matriz[:, -1]
    unicos = np.unique(tipos)
    print("Tipos distintos de vinos:", len(unicos), "->", unicos)
    
    # Apartado 4: Mostrar los valores maximos y minimos de cada caracteristica
    caracteristicas = matriz[:, :-1]
    print("Maximos por caracteristicas:", caracteristicas.max(axis = 0))
    print("Minimos por caracteristicas:", caracteristicas.min(axis = 0))
    
    # Retornar una matriz x con solo las caracteristicas y un nuevo array y con los tipos de vino
    x = matriz[:, -1]
    y = matriz[:, :-1]
    
    return x, y
    
    
    
if __name__ == "__main__":
    imprimir_datos(datos)
    
    x, y = imprimir_datos(datos)
    print("Matriz de caracteristicas de los vinos:", x)
    print("Array con los tipos de vino:", y)