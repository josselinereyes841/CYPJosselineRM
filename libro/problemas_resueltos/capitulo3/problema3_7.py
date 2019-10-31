MED = 0
CHI = 0
GRA = 0
N =int(input("Escribe N: "))
for I in range (1,N+1,1):
    V =float(input("Escribe el valor de V: "))
    if V<=200:
        CHI+= 1
    else:
        if V<400:
            MED +=1
        else:
            GRA += 1
print("CHI", CHI, "MED", MED, "GRA", GRA)
