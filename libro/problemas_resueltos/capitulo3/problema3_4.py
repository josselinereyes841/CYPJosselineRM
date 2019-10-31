NOM = 0
SUE=float(input("Escribe el sueldo del trabajador: "))
while(SUE != 0):
    if SUE < 1000:
        NSUE =SUE *1.15
    else :
        NSUE = SUE *1.12
    NOM += NSUE
    print(f" El nuevo sueldo es de: {NSUE}")
print(f"Nomina es: {NOM}")
