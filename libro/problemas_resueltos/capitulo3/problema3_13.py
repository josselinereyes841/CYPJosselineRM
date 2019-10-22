ARSU = 0
ARNO = 0
MERSU = 50000
MES = 0
ARCE = 0
for i in range(1 , 13 , 1):
    print(f"Mes { i }: ")
    RNO = int(input("promedio de lluvias del mes Zona Norte: "))
    RCE = int(input("promedio de lluvias del mes Zona Centro: "))
    RSU = int(input("promedio de lluvias del mes Zona Sur: "))

    ARNO = ARNO + RNO
    ARCE = ARCE + RCE
    ARSU = ARSU + RSU


    if RSU < MERSU:
        MERSU = RSU
        MES = i
PRORCE = ARCE / 12
print(f"promedio Zona Centro:{PROCE}")
print(f"Mes con menor lluvia en Zona Sur: {MES}")
print(f"Registro del mes con menor lluvia es: {MERSU}")


if ARNO > ARCE:
    if ARNO > ARSU:
        print("La Zona con mayor lluvia es la Zona Norte")
    else:
        print("La region con mayor lluvia es la Zona Sur")
elif ARCE > ARSU:
    print("La Zona con mayores lluvias es la Zona Centro")
else:
    print("La Zona con mayores lluvias es la Zona Sur")

print("Fin del programa!")
