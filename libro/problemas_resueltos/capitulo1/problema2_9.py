PRUEBAS = float(input("Ingrese el valor del producto: "))
if PRUEBAS > 500:
    IMP =  20*0.30 + (PRUEBAS-40)*0.50
    PRETOT = PRUEBAS + IMP
    print(f"El precio del producto es: {PRUEBAS} y el total a pagar es: {PRETOT}")
elif PRUEBAS > 40:
    IMP =  20*0.30 + (PRUEBAS-40)*0.40
    PRETOT = PRUEBAS + IMP
    print(f"El precio del producto es: {PRUEBAS} y el total a pagar es: {PRETOT}")
elif PRUEBAS > 20:
    IMP = (PRUEBAS-20)*0.30
    PRETOT = PRUEBAS + IMP
    print(f"El precio del producto es: {PRUEBAS} y el total a pagar es: {PRETOT}")
else:
    IMP = 0
    PRETOT = PRUEBAS + IMP
    print(f"El precio del producto es: {PRUEBAS} y el total a pagar es: {PRETOT}")
print("fin del programa")
