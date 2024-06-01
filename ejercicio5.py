def suma_numeros_pares():
    """Calcula la suma de todos los números pares del 1 al 100."""
    suma = 0
    for numero in range(1, 101):
        if numero % 2 == 0:
            suma += numero
    return suma

# Ejemplo de uso
total_suma = suma_numeros_pares()
print(f"La suma de todos los números pares del 1 al 100 es: {total_suma}")
