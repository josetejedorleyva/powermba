def dolares_a_euros(dolares):
    """Convierte una cantidad de dólares a euros."""
    tasa_cambio = 0.85
    euros = dolares * tasa_cambio
    return euros

# Ejemplo de uso
dolares = float(input("Introduce la cantidad de dólares a convertir a euros: "))
euros = dolares_a_euros(dolares)
print(f"{dolares} dólares son {euros} euros.")
