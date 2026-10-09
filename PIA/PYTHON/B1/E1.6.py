# Sucesion de Fibonacci hasta N usando asignacion multiple a, b=b, a + b

def fibonacci(n: int) -> list[int]:
    lista = []
    
    a, b = 0, 1
    
    while a <= n:
        lista.append(a)
        a, b = b, a + b
    
    return lista
    
numero = int(input("Introduce un numero para conocer su sucesion de Fibonacci: "))

print(f"La sucesion de Fibonacci del numero {numero} es " , fibonacci(numero))