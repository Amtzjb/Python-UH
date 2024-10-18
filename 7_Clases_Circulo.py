import math

class Circulo():
    def __init__(self,radio):
        self.radio = radio
        
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio
    
circulo_uno = Circulo(5)

#calcular el area del circulo_uno
area = circulo_uno.calcular_area()
print(f"el area del circulo es: {area}")

#circunferencia
circunferencia = circulo_uno.calcular_circunferencia()
print(f"Circunferencia del círculo: {circunferencia}")