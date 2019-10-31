SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
N = int(input("Escribe el número de datos:"))
for i in range (1,N+1, 1):
    NUM = (f"Escribe NUM")
    if NUM > 0:
        SUMPOS += NUM
        CUEPOS += 1
    else :
        SUMOTR += NUM
PROGEN = (SUMPOS + SUMOTR)/N
PROPOS = (SUMPOS/CUEPOS)
print(f"{CUEPOS} {PROPOS} Y {PROGEN}")
