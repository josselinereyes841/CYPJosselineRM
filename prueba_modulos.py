#primera forma de importar (importa todo el archivo)
#import modulos
#modulos.mi_print("Hola")

#segunda forma de importar (te importa las formas internas de interés)
from modulos import mi_print , otro_print , sumar , restar
import time
import sys
from asciistuff import Banner

mi_print("Hola de nuevo")
otro_print("otro print usado")
print(sumar(4 , 5))
print(restar(10 , 7))

for i in range (10,0,-1):
    print(i,"...")
    time.sleep(0.25)
print(Banner("BOOOOOM!!"))


print(sys.platform)
