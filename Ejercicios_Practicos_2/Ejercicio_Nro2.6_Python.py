usuarioregistrado = "admin"
contraseñaregistrada = "admin"

print("--- INICIO DE SESIÓN ---")
print("Ingresar el nombre de usuario:")

usuarioingresado = input()
print("Ingrese la contraseña: ")

contraseñaingresada = input()

if usuarioregistrado == usuarioingresado and contraseñaregistrada == contraseñaingresada:
    print("|-- ACCESO OTORGADO --|")
else:
    print("Error: Usuario o Contraseña incorrectos.")
    
