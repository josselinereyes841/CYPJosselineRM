edad = int(input("Dame tu edad: "))
INE = bool(int(input("Tienes INE (0 No / 1 si)?: ")))

if edad >= 18 and INE == True:
    print("Eres mayor de edad")
    print("puedes enntrar al Bar")

else:
    print("Eres menor de edad")
    print("puedes ir a jugar Lol")
print("Fin del programa")

