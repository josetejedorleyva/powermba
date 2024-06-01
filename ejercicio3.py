def es_mayor_de_edad(edad):
    """Determina si la edad ingresada es mayor o igual a 18 años."""
    if edad >= 18:
        return True
    else:
        return False

# Ejemplo de uso
edad = int(input("Introduce tu edad: "))
if es_mayor_de_edad(edad):
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")
