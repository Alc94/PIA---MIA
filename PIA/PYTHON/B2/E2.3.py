# Agenda: diccionario de contactos con alta, baja, búsqueda y
# listado ordenado, en un bucle de menú.

agenda = {}

# FUNCION PARA DAR DE ALTA A UN CONTACTO
def alta():
    nombre = input("Nombre del contacto: ").strip().title()
    email = input("Email del contacto: ").strip()
    telefono = input("Telefono del contacto: ").strip()
    
    if nombre in agenda:
        print(f"{nombre} ya se encuentra en la agenda")
    else:
        print(f"{nombre} registrado correctamente!!")
        
    agenda[nombre] = {
        "email": email,
        "telefono": telefono
    }
    
# FUNCION PARA DAR DE BAJA A UN CONTACTO
def baja():
    nombre = input("Introduce el nombre del contacto para dar de baja: ").strip().title()
    eliminado = agenda.pop(nombre, None)
    
    if eliminado:
        print(f"Contacto con nombre {nombre}, eliminado correctamente!!!")
    else:
        print(f"Dicho contacto no se encuentra en la agenda...")
        
# FUNCION PARA BUSCAR A UN CONTACTO
def busqueda():
    nombre = input("Introduce el nombre del contacto para su búsqueda: ").strip().title()
    
    if nombre in agenda:
        datos = agenda[nombre]
        print(f"Contacto {nombre}: \nEmail: {datos["email"]}\nTelefono: {datos["telefono"]}")
    else:
        print("El contacto no se encuentra en la agenda...")
    
def agenda_ord():
    
    if not agenda:
        print("La agenda se encuentra vacía...")
    else:
        for nombre in sorted(agenda.keys()):
            datos = agenda[nombre]
            
            print(f"Contacto {nombre}: \nEmail: {datos["email"]}\nTelefono: {datos["telefono"]}")

    
while True:
    print("--- MENÚ AGENDA ---\n1.Alta de un contacto\n2. Baja de un contacto\n3. Búsqueda\n4. Listado ordenado\n5. Salir")
    
    opcion = int(input("Selecciona una opcion del 1 al 5: "))
    
    if opcion == 1:
        alta()
    elif opcion == 2:
        baja()
    elif opcion == 3:
        busqueda()
    elif opcion == 4:
        agenda_ord()
    elif opcion == 5:
            print("Saliendo del menu de agenda...")
            break
    else:
        print("OPCIÓN NO VÁLIDA")
    