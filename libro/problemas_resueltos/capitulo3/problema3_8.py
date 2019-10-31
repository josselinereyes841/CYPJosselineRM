NUM = int(input("Escribe un número: "))
if NUM >0:
    while (NUM != 1) :
        print(f"NUM es: {NUM}")
        if ((-1)**NUM)>0:
            NUM = NUM // 2
        else:
            NUM = NUM*3 + 1
    print(f"El número es {NUM}")
else:
    print(f"El número debe ser un entero positivo")
