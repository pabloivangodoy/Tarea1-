from datetime import datetime

def obtener_fecha(mensaje):
    while True:
        try:
            fecha_str = input(mensaje)
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            return fecha
        except ValueError:
            print("Fecha inválida. Use el formato YYYY-MM-DD.")

def calcular_dias_entre_fechas(fecha1, fecha2):
    return (fecha2 - fecha1).days

def main():
    print("Ingrese la primera fecha:")
    fecha1 = obtener_fecha("Fecha 1 (YYYY-MM-DD): ")
    
    print("Ingrese la segunda fecha:")
    fecha2 = obtener_fecha("Fecha 2 (YYYY-MM-DD): ")

    dias = calcular_dias_entre_fechas(fecha1, fecha2)
    
    print(f"El número de días entre {fecha1.strftime('%Y-%m-%d')} y {fecha2.strftime('%Y-%m-%d')} es: {dias} días")

if __name__ == "__main__":
    main()
