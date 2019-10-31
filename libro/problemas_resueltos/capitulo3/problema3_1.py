SUMPAR=0
SUMIMP =0
CUEPAR =0
for i in range (1,4,1):
    NUM =float(input("Ingresa un numero entero:"))
    if NUM !=0:
        if ((-1)**NUM)>0:
            CUEPAR +=1
            SUMPAR +=NUM
else:
 SUMIMP *=NUM
PROPAR = SUMPAR/CUEPAR
print(f"Los numeros pares son: {PROPAR} y los impares son: {SUMIMP}")

