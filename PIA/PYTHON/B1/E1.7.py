# Conversor seguro: pide un valor e indica si es entero, decimal o no numerico
# convirtiendolo al tipo adecuado
 
def conversor_seguro(valor: str):
    entrada = valor.strip()
     
    try:
         valor_int = int(valor)
         return valor_int, "entero"
    except:
         pass
     
    try:
        valor_float = float(valor)
        return valor_float, "decimal"
    except ValueError:
        pass
    
    return entrada, "no numerico"

variable = input("Introduce un valor: ")

variable_conv, tipo = conversor_seguro(variable)

print(f"Tipo detectado: {tipo}")
print(f"Valor almacenado: {variable_conv} (tipo de dato: {type(variable_conv).__name__})")      