MAT = int(input("Ingrese la matrícula del alumno: "))
print("Ingrese las calificaciones del alumno a continuación:")
CAL1 = float(input(" 1: "))
CAL2 = float(input(" 2: "))
CAL3 = float(input(" 3: "))
CAL4 = float(input(" 4: "))
CAL5 = float(input(" 5: "))
PRO = (CAL1 + CAL2 + CAL3 +CAL4 + CAL5)/5
if PRO >= 6:
    print(f"el alumno: {MAT}, su promedio es: {PRO}, APROBADO")
else:
   print(f"el alumno: {MAT} , su promedio es: {PRO} , NO APROBADO")
print("fin del programa")


