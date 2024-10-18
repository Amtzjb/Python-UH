def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

def calculadora():
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    operacion = input("Ingrese el número de la operación (1/2/3/4): ")
    
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        return "Error: Entrada inválida. Ingrese solo números."

    if operacion == '1':
        print(f"Resultado: {suma(num1, num2)}")
    elif operacion == '2':
        print(f"Resultado: {resta(num1, num2)}")
    elif operacion == '3':
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif operacion == '4':
        print(f"Resultado: {division(num1, num2)}")
    else:
        print("Operación no válida. Intente nuevamente.")

calculadora()
