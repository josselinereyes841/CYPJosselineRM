SUE = float(input("Ingrese el sueldo del trabajador: "))

if SUE < 1000:
    AUM= SUE*0.15
    NSUE = AUM + SUE
    print(NSUE)
else:
    AUM = SUE*0.12
    NSUE = AUM +SUE
    print(NSUE)
