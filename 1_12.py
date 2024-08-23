capital = float(input("Ingresa el capital inicial: "))
tasa = float(input("Ingresa la tasa de interes anual: "))
años = int(input("Ingresa la cantidad de años: "))

interes = capital * tasa * años
Monto_total = capital + interes

print("Interes: " , interes)
print("Monto final: " ,Monto_total)