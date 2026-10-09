print("Ingresar su edad: ")
edad = int(input())
print("Ingrear su sexo (hombre / mujer):")
sexo = input()
if edad >= 16:
    print("Usted es", sexo, "y Puede votar.")
else:
    print("Usted es", sexo, "y No puede votar.")