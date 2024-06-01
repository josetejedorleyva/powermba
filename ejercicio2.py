def calcular_total_con_propina(monto):
    """Calcula el monto total a pagar incluyendo una propina del 15%."""
    propina = monto * 0.15
    total = monto + propina
    return total

# Ejemplo de uso
monto = float(input("Introduce el monto total de la cuenta (sin propina): "))
total_con_propina = calcular_total_con_propina(monto)
print(f"El monto total a pagar, incluyendo una propina del 15%, es: {total_con_propina:.2f}")
