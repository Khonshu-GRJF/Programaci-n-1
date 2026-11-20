# LOGIX -> LOGIX AUTONOMOUS - Prototipo de analisis de impacto
# Trabajo intercatedra: Programacion I, Ingenieria de Requerimientos I y Matematica Discreta
# Alumnos: JuanFra (Galvan Romero Juan Francisco) y Evaristo (Kokotik Evaristo)
# Universidad de la Cuenca del Plata - Ingenieria en Sistemas de Informacion - 1er anio
#
# Requerimientos que implementa:
#   RF-09: Ranking de modulos mas criticos (Warshall + lista de diccionarios + Metodo de Seleccion)
#   RF-11: Guardar el reporte del analisis en un archivo de texto

# ---------------------------------------------------------------
# DATOS DE LOGIX
# ---------------------------------------------------------------

modulos = ["PED", "CLI", "INV", "ROB", "ASG", "RUT", "SEG", "ENT", "REP"]

# matriz_dependencias[i][j] = 1 si el modulo i depende del modulo j
matriz_dependencias = [
    [0, 1, 1, 0, 1, 0, 0, 0, 0],  # PED depende de CLI, INV, ASG
    [0, 0, 0, 0, 0, 0, 0, 0, 0],  # CLI no depende de nadie
    [0, 0, 0, 1, 0, 0, 0, 0, 0],  # INV depende de ROB
    [0, 0, 1, 0, 0, 0, 0, 0, 0],  # ROB depende de INV
    [0, 0, 1, 0, 0, 1, 0, 0, 0],  # ASG depende de INV, RUT
    [0, 0, 0, 0, 0, 0, 1, 0, 0],  # RUT depende de SEG
    [0, 0, 0, 0, 1, 0, 0, 0, 0],  # SEG depende de ASG
    [1, 0, 0, 0, 0, 0, 1, 0, 0],  # ENT depende de PED, SEG
    [1, 0, 1, 0, 0, 0, 0, 1, 0]   # REP depende de PED, INV, ENT
]


# ---------------------------------------------------------------
# FUNCIONES
# ---------------------------------------------------------------

def calcular_alcanzabilidad(matriz):
    """
    Devuelve la matriz de alcanzabilidad A* con el algoritmo de Warshall.
    Regla: si i llega a k y k llega a j, entonces i llega a j.
    """
    n = len(matriz)

    # Primero hago una copia para no modificar la matriz original
    copia = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(matriz[i][j])
        copia.append(fila)

    # Warshall: 3 for anidados (k, i, j)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if copia[i][k] == 1 and copia[k][j] == 1:
                    copia[i][j] = 1
    return copia


def generar_ranking_criticos(modulos, matriz_a, matriz_a_estrella):
    """
    Arma una lista de diccionarios con los datos de cada modulo y la ordena
    de mayor a menor impacto total (si empatan, por cantidad de directos)
    usando el Metodo de Seleccion.
    """
    n = len(modulos)
    ranking = []

    for j in range(n):
        # Directos: suma de la columna j en la matriz original A
        directos = 0
        for i in range(n):
            directos = directos + matriz_a[i][j]

        # Impacto total: suma de la columna j en A*, sin contarse a si mismo
        impacto_total = 0
        for i in range(n):
            if i != j:
                impacto_total = impacto_total + matriz_a_estrella[i][j]

        # Esta en un ciclo si en la diagonal de A* hay un 1
        en_ciclo = matriz_a_estrella[j][j] == 1

        registro = {
            "modulo": modulos[j],
            "directos": directos,
            "impacto_total": impacto_total,
            "en_ciclo": en_ciclo
        }
        ranking.append(registro)

    # Metodo de Seleccion: en cada vuelta busco el mas critico de lo que queda
    # y lo intercambio con la posicion i usando la variable aux
    for i in range(n - 1):
        pos_mayor = i
        for j in range(i + 1, n):
            if ranking[j]["impacto_total"] > ranking[pos_mayor]["impacto_total"]:
                pos_mayor = j
            elif ranking[j]["impacto_total"] == ranking[pos_mayor]["impacto_total"]:
                # Desempate: el que tiene mas dependientes directos va primero
                if ranking[j]["directos"] > ranking[pos_mayor]["directos"]:
                    pos_mayor = j
        if pos_mayor != i:
            aux = ranking[i]
            ranking[i] = ranking[pos_mayor]
            ranking[pos_mayor] = aux

    return ranking


def texto_ciclo(en_ciclo):
    """Devuelve 'SI' o 'NO' para mostrar si el modulo esta en un ciclo."""
    if en_ciclo:
        return "SI"
    else:
        return "NO"


def mostrar_ranking(ranking):
    """Muestra en consola la tabla del RF-09."""
    print("\nRF-09 - RANKING DE MODULOS MAS CRITICOS")
    print("Puesto  Modulo  Directos  Impacto total  En ciclo")
    for i in range(len(ranking)):
        r = ranking[i]
        linea = str(i + 1).rjust(6) + "  " + r["modulo"].ljust(6)
        linea = linea + str(r["directos"]).rjust(10) + str(r["impacto_total"]).rjust(15)
        linea = linea + "  " + texto_ciclo(r["en_ciclo"]).rjust(8)
        print(linea)


def guardar_reporte_txt(ranking, nombre_archivo):
    """RF-11: guarda el ranking, los modulos en ciclo y una recomendacion en un archivo de texto."""
    archivo = open(nombre_archivo, "w")
    archivo.write("REPORTE DE CRITICIDAD DE MODULOS - LOGIX\n")
    archivo.write("========================================\n\n")

    archivo.write("Ranking (de mayor a menor impacto total):\n")
    archivo.write("Puesto  Modulo  Directos  Impacto total  En ciclo\n")
    for i in range(len(ranking)):
        r = ranking[i]
        linea = str(i + 1).rjust(6) + "  " + r["modulo"].ljust(6)
        linea = linea + str(r["directos"]).rjust(10) + str(r["impacto_total"]).rjust(15)
        linea = linea + "  " + texto_ciclo(r["en_ciclo"]).rjust(8)
        archivo.write(linea + "\n")

    # Lista de modulos que estan en ciclos
    en_ciclo = []
    for i in range(len(ranking)):
        if ranking[i]["en_ciclo"]:
            en_ciclo.append(ranking[i]["modulo"])

    archivo.write("\nModulos en dependencias circulares (ciclos): ")
    for i in range(len(en_ciclo)):
        archivo.write(en_ciclo[i])
        if i < len(en_ciclo) - 1:
            archivo.write(", ")
    archivo.write("\n")

    archivo.write("\nRecomendacion (Ingenieria de Requerimientos):\n")
    archivo.write("Priorizar la reestructuracion de los modulos mas criticos y de los que estan\n")
    archivo.write("en ciclos, empezando por " + ranking[0]["modulo"] + " (afecta a ")
    archivo.write(str(ranking[0]["impacto_total"]) + " modulos). Mientras un modulo este en un ciclo\n")
    archivo.write("no se puede cambiar ni migrar sin afectar a los otros modulos del ciclo.\n")
    archivo.close()

    print("Reporte guardado correctamente en " + nombre_archivo)


def menu_principal():
    matriz_a_estrella = calcular_alcanzabilidad(matriz_dependencias)
    ranking = generar_ranking_criticos(modulos, matriz_dependencias, matriz_a_estrella)

    opcion = -1
    while opcion != 0:
        print("\n===== LOGIX - Analisis de impacto =====")
        print("1. Ver ranking de modulos criticos (RF-09)")
        print("2. Guardar reporte en archivo de texto (RF-11)")
        print("0. Salir")
        texto = input("Elegir opcion: ").strip()

        if texto == "1":
            opcion = 1
            mostrar_ranking(ranking)
        elif texto == "2":
            opcion = 2
            guardar_reporte_txt(ranking, "reporte_criticidad.txt")
        elif texto == "0":
            opcion = 0
            print("Fin del programa.")
        else:
            print("Opcion invalida. Ingrese 1, 2 o 0.")


menu_principal()
