BAND = 'T'
SUMSER = 0
I = 2
while (I<= 1800):
    SUMSER += 1
    print (I)
    if BAND == 'T':
        BAND = 'F'
        I += 3
    else:
        BAND ='T'
        I += 2
print(f"SUMSER {SUMSER}")
