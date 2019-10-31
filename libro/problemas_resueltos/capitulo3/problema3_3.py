SERIE = 0
N= int(input("Escribe un número: "))
BAND = True
I = 1
for I in range (1,N+1,1):
    if BAND == True:
        SERIE += 1/I
        BAND = False
    else:
        SERIE += -1/I
        BAND = True
    I+=1
print(f"La serie es {SERIE}: ")
