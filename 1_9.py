año = int(input("Ingrese un año: "))

año_viciesto1 = año % 4
año_viciesto2 = año % 100
año_viciesto3 = año % 400

if año_viciesto1 == 0 or año_viciesto3 == 0 and año_viciesto2 != 0 :
    print(año ," es un año biciesto.")
else:
    print(año ," no es un año biciesto.") 