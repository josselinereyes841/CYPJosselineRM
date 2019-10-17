COMPRA = float(input("Ingrese el calor de la compra: "))

if COMPRA < 500:
    PAGAR = COMPRA
    print(f"Puede pagar la cantidad de: {COMPRA}")
elif COMPRA <= 1000:
    PAGAR = COMPRA - (COMPRA*0.05)
    print(f"La cantidad a pagar es: {PAGAR}")
elif COMPRA <= 7000:
    PAGAR = COMPRA = COMPRA - (COMPRA*0.11)
    print(f"La cantidad a pagar es: {PAGAR}")
elif COMPRA <= 15000:
    PAGAR = COMPRA - (COMPRA*0.18)
    print(f"La cantidad a pagar es: {PAGAR}")
else:
    PAGAR = COMPRA - (COMPRA*0.25)
    print(f"La cantidad a pagar es: {PAGAR}")
print("fin del programa")

