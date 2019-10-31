MAY = -100000
MEN = 100000
N = int(input("Escribe N"))
for I in range (1,N+1,1):
    NUM = int(input("Escribe NUM: "))
    if NUM > MAY:
        MAY = NUM
    if NUM < MEN :
        MEN = NUM
print("MAY ES: ",MAY,"MEN ES: ",MEN,)

