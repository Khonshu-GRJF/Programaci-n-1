import json
import os


def cargar_ventas():
    ventas = {}
    if os.path.exists("ventas.json"):
        with open("ventas.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        for dia in datos:
            ventas[int(dia)] = {}
            for codigo in datos[dia]:
                ventas[int(dia)][int(codigo)] = datos[dia][codigo]
    return ventas


def calcular_totales_productos(productos, ventas):
    totales = {cod: 0 for cod in productos}
    for dia in ventas:
        for codigo, cantidad in ventas[dia].items():
            totales[codigo] += cantidad
    return totales


def calcular_recaudacion_dia(productos, ventas, dia):
    recaudacion = 0
    if dia in ventas:
        for codigo, cantidad in ventas[dia].items():
            recaudacion += cantidad * productos[codigo]["precio"]
    return recaudacion




def guardar_ventas(ventas):
    
    with open("ventas.json", "w", encoding="utf-8") as archivo:
        json.dump(ventas, archivo, ensure_ascii=False, indent=4)


def mostrar_menu():
    print("\n BUFFET DE LA FACULTAD ")
    print("1. Registrar venta")
    print("2. Ver informes de la semana")
    print("3. Salir")


def registrar_venta(productos, ventas):
    print("\n REGISTRAR VENTA")
    try:
        dia = int(input("Ingrese el día (1=Lunes a 5=Viernes): "))
        if dia < 1 or dia > 5:
            print("Día inválido. Debe ser entre 1 y 5.")
            return

        codigo = int(input("Ingrese el código del producto (101-106): "))
        if codigo not in productos:
            print("El código de producto no existe.")
            return

        cantidad = int(input("Ingrese la cantidad vendida: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        
        if dia not in ventas:
            ventas[dia] = {}

        
        if codigo in ventas[dia]:
            ventas[dia][codigo] += cantidad
        else:
            ventas[dia][codigo] = cantidad

        guardar_ventas(ventas)
        print("¡Venta registrada con éxito!")

    except ValueError:
        print("Error: Ingrese solo números enteros válidos.")


def mostrar_informes(productos, ventas):
    if not ventas:
        print("\nNo hay ventas registradas todavía.")
        return

    print("\n INFORMES DE LA SEMANA ")

    dias_nombres = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes"}
    totales_productos = calcular_totales_productos(productos, ventas)

    
    print("\n1. Unidades vendidas por producto:")
    for codigo, info in productos.items():
        print(f" - {info['nombre']}: {totales_productos[codigo]} unidades")

    
    print("\n2. Recaudación de cada día:")
    recaudaciones = {}
    recaudacion_total_semana = 0
    for d_num in range(1, 6):
        recaudaciones[d_num] = calcular_recaudacion_dia(productos, ventas, d_num)
        recaudacion_total_semana += recaudaciones[d_num]
        print(f" - {dias_nombres[d_num]}: ${recaudaciones[d_num]}")

    print("\n3. Producto más vendido y día de mayor recaudación:")
    mayor_cantidad = 0
    for codigo in totales_productos:
        if totales_productos[codigo] > mayor_cantidad:
            mayor_cantidad = totales_productos[codigo]
    for codigo in totales_productos:
        if totales_productos[codigo] == mayor_cantidad:
            print(f" - Producto más vendido: {productos[codigo]['nombre']} ({mayor_cantidad} unidades)")

    mayor_recaudacion = 0
    for d_num in recaudaciones:
        if recaudaciones[d_num] > mayor_recaudacion:
            mayor_recaudacion = recaudaciones[d_num]
    for d_num in recaudaciones:
        if recaudaciones[d_num] == mayor_recaudacion:
            print(f" - Día de mayor recaudación: {dias_nombres[d_num]} (${mayor_recaudacion})")

    print("\n4. Productos sin ventas en la semana:")
    hay_sin_ventas = False
    for codigo in productos:
        vendido = False
        for dia in ventas:
            if codigo in ventas[dia]:
                vendido = True
                break  
        if not vendido:
            print(f" - {productos[codigo]['nombre']}")
            hay_sin_ventas = True
    if not hay_sin_ventas:
        print(" - Todos los productos se vendieron al menos una vez.")

    print(f"\n5. Recaudación total de la semana: ${recaudacion_total_semana}")



def main():
    productos = {
        101: {"nombre": "Café con leche", "precio": 1500},
        102: {"nombre": "Medialuna", "precio": 700},
        103: {"nombre": "Sándwich de miga", "precio": 1800},
        104: {"nombre": "Agua mineral 500 ml", "precio": 1000},
        105: {"nombre": "Empanada", "precio": 1200},
        106: {"nombre": "Chipá (100 g)", "precio": 1300}
    }

    ventas = cargar_ventas()

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            registrar_venta(productos, ventas)
        elif opcion == "2":
            mostrar_informes(productos, ventas)
        elif opcion == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


main()