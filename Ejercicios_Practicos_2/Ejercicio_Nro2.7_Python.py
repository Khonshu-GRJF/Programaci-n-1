from math import pi

print("--- MENÚ DE OPCIONES---")
print("1- Circulo (Perímetro y Área)")
print("2- Pentágono (Perímetro y Área)")
print("3- Rectángulo (Perímetro y Área)")
print("Seleccione un opción (1-3): ")
eleccion = int(input())

if eleccion == 1:
    print("Ingrese el radio del círculo:")
    radio =float(input())
    perimetro = (2 * pi *radio)
    area = pi * (radio ** 2)
    print("Perímetro:", perimetro)
    print("Área:", area)
elif eleccion == 2:
    print("Lado: ")
    lado = float(input())
    print("Ingrese la apotema del pentágono:")
    apotema = float(input())
    perimetro = (5 * lado)
    area = ((perimetro * apotema) / 2)
    print("Perímetro: ", perimetro)
    print("Área: ", area)
elif eleccion == 3:
    print("Ingrese la base del rectángulo:")
    base = float(input())
    print("Ingrese la altura del rectángulo:")
    altura = float(input())
    perimetro = (2 * (base + altura))
    area = (base * altura)
    print("Perímetro:", perimetro)
    print("Área:", area)
else:
    print("Opción no válida.")
    