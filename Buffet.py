import json
import os


def main():
    #1.Catálogo inicial de productos (código como clave, nombre y precio)
    productos = {
        101: {"nombre": "Café con leche", "precio": 1500},
        102: {"nombre": "Medialuna", "precio": 700},
        103: {"nombre": "Sándwich de miga", "precio": 1800},
        104: {"nombre": "Agua mineral 500 ml", "precio": 1000},
        105: {"nombre": "Empanada", "precio": 1200},
        106: {"nombre": "Chipá (100 g)", "precio": 1300}
    }
    
    #Estructura para ventas: { día (1 al 5): { código_producto: cantidad } }
    ventas = {}
    
    
    if os.path.exists("ventas.json"):
        with open("ventas.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            
        for dia in datos:
            ventas[int(dia)] = {}
            for codigo in datos[dia]:
                ventas[int(dia)][int(codigo)] = datos[dia][codigo]
    
    #2.Menú principal usando un bucle while
    while True:
        print("\n BUFFET DE LA FACULTAD ")
        print("1. Registrar venta")
        print("2. Ver informes de la semana")
        print("3. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            print("\n--- REGISTRAR VENTA ---")
            try:
                dia = int(input("Ingrese el día (1=Lunes a 5=Viernes): "))
                if dia < 1 or dia > 5:
                    print("Día inválido. Debe ser entre 1 y 5.")
                    continue
                
                codigo = int(input("Ingrese el código del producto (101-106): "))
                if codigo not in productos:
                    print("El código de producto no existe.")
                    continue
                
                cantidad = int(input("Ingrese la cantidad vendida: "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue
                
                #Inicializar el día si no existe en el diccionario de ventas
                if dia not in ventas:
                    ventas[dia] = {}
                
                if codigo in ventas[dia]:
                    ventas[dia][codigo] += cantidad
                else:
                    ventas[dia][codigo] = cantidad

                with open("ventas.json", "w", encoding="utf-8") as archivo:
                    json.dump(ventas, archivo, ensure_ascii=False, indent=4)

                print("¡Venta registrada con éxito!")
                
            except ValueError:
                print("Error: Ingrese solo números enteros válidos.")
                
        elif opcion == "2":
            if not ventas:
                print("\nNo hay ventas registradas todavía.")
                continue
            
            print("\n INFORMES DE LA SEMANA ")
            
            #Inicializar acumuladores para los productos
            totales_productos = {cod: 0 for cod in productos}
            recaudacion_total_semana = 0
            
            #Nombres de los días para mostrar de forma clara
            dias_nombres = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes"}
            
            print("\n1. Unidades vendidas por producto:")
            for dia in ventas:
                for codigo, cantidad in ventas[dia].items():
                    totales_productos[codigo] += cantidad
            
            for codigo, info in productos.items():
                print(f" - {info['nombre']}: {totales_productos[codigo]} unidades")
            
            print("\n2 y 5. Recaudación de cada día y total:")
            for d_num in range(1, 6):
                recaudacion_dia = 0
                if d_num in ventas:
                    for codigo, cantidad in ventas[d_num].items():
                        recaudacion_dia += cantidad * productos[codigo]["precio"]
                
                recaudacion_total_semana += recaudacion_dia
                nombre_dia = dias_nombres[d_num]
                print(f" - {nombre_dia}: ${recaudacion_dia}")
            
            print(f" -> Recaudación total de la semana: ${recaudacion_total_semana}")
            
        elif opcion == "3":
            print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
main()