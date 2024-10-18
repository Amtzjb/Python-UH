class CuentaBancaria():
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
        
    def Depositar(self,monto):
        if monto > 0:
            self.saldo += monto
            print(f"Has depositado la cantidad de: {monto}, su saldo es de: {self.saldo} ")
        else:
            print("El monto a deposita debe ser mayor a 0")
            
    def Retirar(self,monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"Se ha retirado la cantidad de {monto} ahora su saldo es de: {self.saldo}")
            else:
                print("saldo insuficiente")
                
    def Consultarsaldo(self):
        print(f"Su saldo es de  {self.saldo}")
        
        
# hora de crear la cuenta bancaria 
mi_cuenta = CuentaBancaria("Angelo Talegon",5000)
print()
#primero veremos mi saldo
mi_cuenta.Consultarsaldo()
print()
# le metemos dinero para la cariñosa
mi_cuenta.Depositar(1500)
print()
#retiramos por que debemos pagar la cariñosa
mi_cuenta.Retirar(1500)
print()
#Intentamos retirar una cantidas mayor al saldo disponible
mi_cuenta.Retirar(6000)

