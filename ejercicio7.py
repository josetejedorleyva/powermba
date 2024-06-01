def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

def main():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    eleccion = input("Introduce el número de la operación (1/2/3/4): ")
    
    if eleccion in ['1', '2', '3', '4']:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        if eleccion == '1':
            print(f"El resultado de la suma es: {suma(num1, num2)}")
        elif eleccion == '2':
            print(f"El resultado de la resta es: {resta(num1, num2)}")
        elif eleccion == '3':
            print(f"El resultado de la multiplicación es: {multiplicacion(num1, num2)}")
        elif eleccion == '4':
            resultado = division(num1, num2)
            print(f"El resultado de la división es: {resultado}")
    else:
        print("Operación no válida. Por favor, introduce un número del 1 al 4.")

if __name__ == "__main__":
    main()
