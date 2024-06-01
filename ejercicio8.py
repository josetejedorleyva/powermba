def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC)."""
    return peso / (altura ** 2)

def main():
    peso = float(input("Introduce tu peso en kilogramos: "))
    altura = float(input("Introduce tu altura en metros: "))

    imc = calcular_imc(peso, altura)
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

    if imc < 18.5:
        print("Tienes un peso bajo.")
    elif imc < 25:
        print("Tienes un peso saludable.")
    elif imc < 30:
        print("Tienes sobrepeso.")
    else:
        print("Tienes obesidad.")

if __name__ == "__main__":
    main()
