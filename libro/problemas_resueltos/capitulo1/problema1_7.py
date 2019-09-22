L1 = float(input("Primer lado: "))
L2 = float(input("Segundo lado: "))
L3 = float(input("Tercer lado: "))
S = (L1+L2+L3)/2
AREA = (S*(S-L1)*(S-L2)*(S-L3))**0.5
print(f"El area del triángulo es: {AREA}")
