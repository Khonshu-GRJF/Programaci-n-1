print("Ingrese el día:")
dia = int(input())

print("Ingrese el mes (1 a 12):")
mes = int(input())

print("Ingrese el año:")
anio = int(input())

esValida = True

if dia < 1 or dia > 31 or mes < 1 or mes > 12 or anio < 0:
    esValida = False
else: 
    if mes in (1, 3, 5, 7, 8, 10, 12):
        if dia > 31: 
            esValida = False
    elif mes == 2:
        if dia > 28:
            esValida = False
    elif mes in (4, 6, 9, 11):
        if dia > 30:
            esValida
if esValida: 
    if mes == 1:
        nombremes = "Enero"
    elif mes == 2:
        nombremes = "Febrero"
    elif mes == 3: 
        nombremes = "Marzo"
    elif mes == 4:
        nombremes = "Abril"
    elif mes == 5: 
        nombremes = "Mayo"
    elif mes == 6: 
        nombremes = "Junio"
    elif mes == 7: 
        nombremes = "Julio"
    elif mes == 8:
        nombremes = "Agosto"
    elif mes == 9:
        nombremes = "Septiembre"
    elif mes == 10:
        nombremes = "Octubre"
    elif mes == 11:
        nombremes = "Noviembre"
    elif mes == 12:
        nombremes = "Diciembre"
        
    print("Fecha válida:", dia, "/", nombremes, "/", anio, sep="")
else:
    print("Error: La fecha ingresada es incorrecta.")   
    