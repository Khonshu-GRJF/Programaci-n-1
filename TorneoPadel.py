#Objetivos de la semana: Introducir la estructura de datos en memoria mediante arreglos unidimensionales (vectores). Aplicar las operaciones básicas con vectores: inicialización, carga de datos por teclado y recorrido.

#Ningún torneo empieza con los jugadores ya anotados por arte de magia. Nuestro sistema necesita un módulo de inscripción para que el juez registre a los competidores antes de repartir puntos.

#Para poder poner en marcha el torneo, lo primero que necesitamos del sistema es
#poder cargar a los jugadores y luego armar las parejas que van a
#competir. Recuerden que en el pádel se juega de a dos: ninguna pareja puede
#tener más ni menos de 2 jugadores.

#a) Ingreso de jugadores

 #Al iniciar el programa, el sistema debe preguntarle al juez:
  #"¿Cuántos jugadores van a participar en el torneo?".
#A partir de esa respuesta, debe permitir registrar cada competidor, uno por
 # uno, con la siguiente información:
  # su nombre (con el que se lo identificará dentro del torneo), y
 #  su categoría (el nivel en el que juega, por ejemplo 4ª, 5ª o 6ª).

#b) Armado de parejas

 #Una vez cargados todos los jugadores, el sistema debe permitir formar las
 # parejas del torneo.
 #Cada pareja debe tener:
  # un nombre que la identifique dentro del torneo (por ejemplo,
  #  "Los Tanos"), y
   #exactamente 2 jugadores, elegidos entre los que ya fueron inscriptos.
   
def cargar_jugadores():
    jugadores = []
    cantidad = int(input("¿Cuántos jugadores van a participar en el torneo? "))
    
    for i in range(cantidad):
        print(f"\nRegistro del jugador {i + 1}:")
        nombre = input("Ingrese el nombre del jugador: ")
        categoria = input("Ingrese la categoría del jugador (por ejemplo 4ª, 5ª o 6ª): ")
        jugadores.append({"nombre": nombre, "categoria": categoria})
    
    return jugadores

def armar_parejas(jugadores):
    parejas = []
    cantidad_parejas = len(jugadores) // 2
    
    for i in range(cantidad_parejas):
        print(f"\nRegistro de la pareja {i + 1}:")
        nombre_pareja = input("Ingrese el nombre de la pareja: ")
        
        print("Seleccione los jugadores para esta pareja:")
        for j, jugador in enumerate(jugadores):
            print(f"{j + 1}. {jugador['nombre']} ({jugador['categoria']})")
        
        indices_jugadores = []
        while len(indices_jugadores) < 2:
            indice = int(input(f"Seleccione el jugador {len(indices_jugadores) + 1} (1-{len(jugadores)}): ")) - 1
            if indice < 0 or indice >= len(jugadores) or indice in indices_jugadores:
                print("Selección inválida. Intente nuevamente.")
            else:
                indices_jugadores.append(indice)
        
        pareja = {
            "nombre": nombre_pareja,
            "jugadores": [jugadores[indices_jugadores[0]], jugadores[indices_jugadores[1]]]
        }
        parejas.append(pareja)
    
    return parejas

def guardar_jugadores(jugadores):
    with open("jugadores.txt", "w", encoding="utf-8") as archivo:
        for jugador in jugadores:
            archivo.write(f"{jugador['nombre']} - {jugador['categoria']}\n")

def guardar_parejas(parejas):
    with open("parejas.txt", "w", encoding="utf-8") as archivo:
        for pareja in parejas:
            jugador1 = pareja["jugadores"][0]["nombre"]
            jugador2 = pareja["jugadores"][1]["nombre"]
            archivo.write(f"{pareja['nombre']}: {jugador1} y {jugador2}\n")


jugadores = cargar_jugadores()
parejas = armar_parejas(jugadores)

guardar_jugadores(jugadores)
guardar_parejas(parejas)

print("Los jugadores se guardaron en jugadores.txt")
print("Las parejas se guardaron en parejas.txt")



   
   

