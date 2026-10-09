# Con range: multiplos de 7 hasta 100, cuenta atras de 10
# a 0 y suma de los pares hasta 1000

# Multiplos de 7 hasta 100
print("---- MULTIPLOS DE 7 HASTA EL 100 ----")

for i in range(101):
    if i % 7 == 0:
        print(f"{i}", end=" ")
        

# Cuenta atras de 10 a 0
print()
print("---- CUENTA ATRAS DE 10 A 0 ----")

for i in range(10, -1, -1):
    print(f"{i}", end=" ")
    

# Suma de los pares hasta 1000
print()

print("---- SUMA DE LOS PARES HASTA 1000 ----")

suma = 0
for i in range(1001):
    if i % 2 == 0:
        suma += i
        
print(f"La suma total es de: {suma}")