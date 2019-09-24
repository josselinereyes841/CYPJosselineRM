NUM1 = int(input("Dame un numero: "))
NUM2 = int(input("Dame un segundo numero: "))
NUM3 = int(input("Dame un tercer numero: "))

if NUM1 > NUM2 and NUM1 > NUM3:
    print(f"{NUM1} es el número más grande")
if NUM2 > NUM1 and NUM2 > NUM3:
    print(f"{NUM2} es el número más grande")
if NUM3 > NUM1 and NUM3 > NUM2:
    print(f"{NUM3} es el número más grande")


