print("Ingrese los siguientes valores: ")
A = float(input("1: "))
B = float(input("2: "))
C = float(input("3: "))
DIS =  B**2-4*A*C
if DIS >= 0:
    x1 = ((-B) + DIS**0.5)/(2*A)
    x2 = ((-B) - DIS**0.5)/(2*A)
    print(f"x1 ={x1} , x2 ={x2}")
print("Fin del programa ")
