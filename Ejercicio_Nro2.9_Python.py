print("Ingrese la cantidad de horas trabajadas:")
horastrabajadas = float(input())

print("Ingrese la tarifa fija por hora:")
tarifahora = float(input())

if horastrabajadas <= 35:
    sueldobruto = horastrabajadas * tarifahora
else:
    horastrabajadas = 35 
    horasextras = horastrabajadas - 35
    sueldobruto = (horastrabajadas * tarifahora) + (horasextras * tarifahora * 1.5)
if sueldobruto < 200000:
    impuesto = 0 
else:
    impuesto = sualdobruto * 0.20
    
sueldoneto = sueldobruto - impuesto

print("--- LIQUIDACIÓN DE SUELDO ---")
print("Sueldo Bruto: $", sueldobruto, sep="")
print("Descuento por Impuestos (20%): $", impuesto, sep="")
print("Sueldo Neto a Cobrar: $", sueldoneto, sep="")