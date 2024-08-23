def obtener_tasa_impuesto():
    while True:
        try:
            tasa_impuesto = float(input("Ingrese la tasa de impuesto en porcentaje: "))
            if 0 <= tasa_impuesto <= 100:
                return tasa_impuesto
            else:
                print("La tasa de impuesto debe estar entre 0 y 100%. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

while True:
    try:
        monto = float(input("Ingrese el monto a pagar: "))
        if monto > 0:
            break
        else:
            print("El monto debe ser mayor que 0. Inténtelo de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

# Obtener la tasa de impuesto del usuario
tasa_impuesto = obtener_tasa_impuesto()

# Calcular el impuesto y el total a pagar
impuesto = monto * (tasa_impuesto / 100)
total = monto + impuesto

# Imprimir el total a pagar
print(f"El total a pagar es de {total:.2f}")
