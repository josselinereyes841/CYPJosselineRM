SERIE= 0
N = int(input("Escribe el valor de N: "))
for I in range(1,N+1,1):
    SERIE += I**I
    I += 1
print (f" SERIE ES IGUAL A {SERIE}")
