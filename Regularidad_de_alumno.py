#Crear una solucion logica estructurada en python usando arreglos, registros y funcoines. para la siguente pregunta.


#¿ Yo quiero saber cuando uno de los siguentes alumnos esta o no esta regular ?

alumnos = [
    { "nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 90 },
    { "nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 60 },
    { "nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 95 },
    { "nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 85 }
]

#hacer una funcion que calcule la regularidad de los alumnos
#Necesitamos tener las 4 notas alumnos para poder determinar si estan regulares o no.
#Y saber el % de asistencia de cada alumno.

#hacer funcion para determinar promedio de un alumno
def calcular_promedio(notas):
    suma=sum(notas)
    cantidad=len(notas)
    promedio=suma/cantidad
    return promedio

#hacer funcion para determinar regularidad de un alumno
def es_regular(alumno):
    promedio = calcular_promedio(alumno["notas"])
    asistencia = alumno["asistencia"]
    
    if promedio >= 6 and asistencia >= 70:
        return True
    else:
        return False
    
  
#muestra por pantalla cada alumno, su promedio de notas, su % de asistencia y si esta regular o no.
for alumno in alumnos:
    promedio = calcular_promedio(alumno["notas"])
    regular = es_regular(alumno)

    print(f"Alumno: {alumno['nombre']}")
    print(f"Promedio de notas: {promedio}")
    print(f"Asistencia: {alumno['asistencia']}%")

    if regular:
        print("Estado: ESTÁ REGULAR")
    else:
        print("Estado: NO ESTÁ REGULAR")
 




