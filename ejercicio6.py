def es_palindromo(palabra):
    """Verifica si la palabra es un palíndromo."""
    palabra = palabra.replace(" ", "").lower()  # Elimina espacios y convierte a minúsculas
    return palabra == palabra[::-1]

# Ejemplo de uso
palabra = input("Introduce una palabra: ")
if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")
