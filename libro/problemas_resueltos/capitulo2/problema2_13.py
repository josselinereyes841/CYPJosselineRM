print("Ingrese los siguientes datos")
MAT = int(input("Matricula del alumno: "))
CARR = str(input("Carrera en la que esta inscrito: "))
SEM = int(input("Semestre: "))
PROM = float(input("Promedio del alumno: "))
if CARR == 'Economia':
    if SEM >= 6 and PROM >= 8.8:
     print(f"El alumno: {MAT} de la carrera: {CARR}, ACEPTADO ")
elif CARR == 'Computacion':
    if SEM > 6 and PROM > 8.5:
        print(f"El alumno: {MAT} de la carrera {CARR}, ACEPTADO")
elif CARR == 'Contabilidad':
    if SEM > 5 and PROM > 8.5:
     print(f"El alumno: {MAT} de la carrera {CARR}, ACEPTADO")
else:
     print("fin del programa")
