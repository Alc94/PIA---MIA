# E4.1

class CuentaBancaria:

    def __init__(self, titular, saldo = 0.0):

        self.titular = titular

        self._saldo = saldo

    """ GETTER """
    @property
    def saldo(self):
        return self._saldo

    def retirar(self, cantidad):
        if cantidad <= 0 or self.saldo - cantidad < 0:
            raise ValueError("La cantidad a retirar debe ser positiva...")
        else:
            self._saldo -= cantidad
            return cantidad

    def ingresar(self, cantidad):
        if cantidad < 1:
            raise ValueError("La cantidad a ingresar no puede ser negativa...")
        else:
            self._saldo += cantidad

try:
    cuenta = CuentaBancaria("Alejandro", 1000.0)
    print(f"El saldo de {cuenta.titular} es de {cuenta.saldo} euros.")

    cuenta.retirar(-500)
    print(f"El saldo es de: {cuenta.saldo}")

    cuenta.ingresar(10)
    print(f"El saldo es de: {cuenta.saldo}")

except ValueError:
    print("ERROR! El número indicado es erróneo...")