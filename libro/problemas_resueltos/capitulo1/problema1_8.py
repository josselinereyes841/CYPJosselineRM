print("Escriba las coordenadas de P1(X1,Y1) Y P2(X2,Y2) para calcular la distancia entre los dos puntos")
X1 = float(input("X1: "))
Y1 = float(input("Y1: "))

X2 = float(input("X2: "))
Y2 = float(input("Y2: "))
D = ((X1 -X2)**2+(Y1-Y2)**2)**0.5
print(f"La distancia entre P1 y P2 es: {D} ")

