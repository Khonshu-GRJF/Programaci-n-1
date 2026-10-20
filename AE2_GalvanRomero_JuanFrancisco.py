import json
import os

def cargar_jugadores(jugadores):
    cantidad = int(input("¿Cuántos jugadores querés cargar ahora?"))
    
    for i in range(cantidad):
        print(f"\nRegistro del jugador {i + 1}:")
        nombre = input("Ingrese el nombre del jugador: ")
        categoria = input("Ingrese la categoría del jugador (1ra, 2da, 3ra, 4ta, 5ta, 6ta, 7ma u 8va): ")
        
        repetido = False
        for jugador in jugadores:
            if jugador["nombre"] == nombre:
                repetido = True
                
        
        if nombre == "":
            print("El nombre no puede estar vacío. Jugador no cargado.")
        elif categoria not in ["1ra", "2da", "3ra", "4ta", "5ta", "6ta", "7ma", "8va"]:
            print("Categoría inválida: Debe ser de 1ra a 8va.Jugador no cargado.")
        elif repetido:
            print("Ya existe un jugador con ese nombre. Jugador no cargado.")
        else:
            jugadores.append({"nombre": nombre, "categoria": categoria})
            print("Jugador cargado exitosamente.")
            
            
def armar_parejas(jugadores, parejas):
    libres = []
    for jugador in jugadores:
        encontrado = False
        for pareja in parejas:
            if jugador["nombre"] in pareja["jugadores"]:
                ocupado = true
        if not ocupado: 
            libres.append(jugador)
            
    cantidad_parejas = len(libres) // 2
    if cantidad_parejas == 0:
        print("No hay suficientes jugadores libres para armar una pareja.")
        
    for i in range(cantidad_parejas):
        print(f"\nRegistro de la pareja {i + 1}:")
        
        repetido = True
        while repetido:
            nombre_pareja = input("Ingrese el nombre de la pareja: ")
            repetido = nombre_pareja == ""
            for pareja in parejas:
                if pareja["nombre"] == nombre_pareja:
                    repetido = True
                    
            if repetido:
                print("El nombre está vacío o ya existe. Intente nuevamente.")
                
        print("Seleccione los jugadores para esta pareja:")
        for j, jugador in enumerate(libres):
            print(f"{j + 1}. {jugador['nombre']} ({jugador['categoria']})")
            
        indices_jugadores = []
        while len(indices_jugadores) < 2:
            indice = int(input(f"Seleccione el jugador {len(indices_jugadores) + 1} (1-{len(libres)}): ")) - 1
            if indice < 0 or indice >= len(libres) or indice in indices_jugadores:
                print("Selección inválida. Intente nuevamente.")
            else:
                indices_jugadores.append(indice)
        
        jugador1 = libres[indices_jugadores[0]]
        jugador2 = libres[indices_jugadores[1]]
        
        
        pareja ={
            "nombre": nombre_pareja,
            "jugadores": [jugador1["nombre"], jugador2["nombre"]]
        }
        parejas.append(pareja)
        
        libres.remove(jugador1)
        libres.remove(jugador2)
        
def registrar_partido(parejas, partidos):
    if len(parejas) < 2:
        print("Se necesitan al menos 2 parejas para registrar un partido.")
    else:
        for i, pareja in enumerate(parejas):
            print(f"{i + 1}. {pareja['nombre']} ({pareja['jugadores'][0]} y {pareja['jugadores'][1]})")
            
            
        p1 = int(input("Número de pareja 1: ")) - 1
        p2 = int(input("Número de pareja 2: ")) - 1
        
        if p1 < 0 or p1 >= len(parejas) or p2 < 0 or p2 >= len(parejas):
            print("Número Inválido.")
        elif p1 == p2:
            print("Elegir dos parejas distintas.")
        else:
            ganador = int(input("Número de la pareja ganadora: ")) - 1
            if ganador != p1 and ganador != p2:
                print("La pareja ganadora debe ser una de las dos paregas")
            else:
                partidos.append({
                    "pareja1": parejas[p1]["nombre"],
                    "pareja2": parejas[p2]["nombre"],
                    "ganador": parejas[ganador]["nombre"]
                })
                print("Partido Registrado.")
                
if os.path.exists("jugadores.json"):
    with open("jugadores.json", "r", encoding="utf-8") as archivo:
        jugadores = json.load(archivo)
else:
    jugadores = []
    
if os.path.exists("parejas.json"):
    with open("parejas.json", "r", encoding="utf-8") as archivo:
        parejas = json.load(archivo)
else:
    parejas = []
    
if os.path.exists("partidos.json"):
    with open("partidos.json", "r", encoding="utf-8") as archivo:
        partidos = json.load(archivo)
else:
    partidos = []
    
opcion = ""
while opcion != "0":
    print("\nMenú de opciones:")
    print("1. Cargar jugadores")
    print("2. Armar parejas")
    print("3. Registrar partido")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        cargar_jugadores(jugadores)
    elif opcion == "2":
        armar_parejas(jugadores, parejas)
    elif opcion == "3":
        registrar_partido(parejas, partidos)
    elif opcion == "0":
        print("Programa cerrado.")
    else:
        print("Opción inválida.")
        
        
with open("jugadores.json", "w", encoding="utf-8") as archivo:
    json.dump(jugadores, archivo, ensure_ascii=False, indent=4)
    
with open("parejas.json", "w", encoding="utf-8") as archivo:
    json.dump(parejas, archivo, ensure_ascii=False, indent=4)   
    
with open("partidos.json", "w", encoding="utf-8") as archivo:
    json.dump(partidos, archivo, ensure_ascii=False, indent=4)  

            
            
            
            