lado1 = float(input("Ingrese la medida del lado 1: "))
lado2 = float(input("Ingrese la medida del lado 2: "))
lado3 = float(input("Ingrese la medida del lado 3: "))

if lado1 == lado2 and lado2 == lado3:
    print("El triangulo es equilatero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("El triangulo es isoceles")
else:
    print("El triangulo es escaleno")