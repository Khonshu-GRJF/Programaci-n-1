print("Ingrese la cantidad de bancos existentes: ")
cantbancos = int(input())
print("Ingrese la cantidad de alumnos inscriptos: ")
cantalumnos = int(input())

if cantbancos >= cantalumnos:
    print("Los bancos alcanzan para todos los alumnos.")
else:
    faltantes = cantalumnos - cantbancos
    print("Los bancos no alcanzan. Se necesitan agregar", faltantes, "banco/s.")