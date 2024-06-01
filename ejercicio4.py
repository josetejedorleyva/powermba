def contar_vocales(palabra):
    """Cuenta el número de vocales en la palabra dada."""
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

# Ejemplo de uso
palabra = input("Introduce una palabra: ")
numero_vocales = contar_vocales(palabra)
print(f"El número de vocales en '{palabra}' es: {numero_vocales}")
