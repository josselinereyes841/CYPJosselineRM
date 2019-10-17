print("Ingrese los siguientes datos de los pacientes")
TIPOENF = int(input("Tipo de enfermedad: "))
EDAD = int(input("Edad: "))
DIAS = int(input("Dias de hospitalizacion: "))
if TIPOENF == 1:
    COSTOT = DIAS*25
elif TIPOENF == 2:
    COSTOT = DIAS*16
elif TIPOENF == 3:
    COSTOT = DIAS*20
elif TIPOENF == 4:
    COSTOT = DIAS*32

if EDAD >= 14 and EDAD <= 22:
    COSTOT = COSTOT*1.10
    print(f"Costo total: {COSTOT}")   
