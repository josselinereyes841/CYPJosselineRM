archivo = open("numeros.txt","rt")
#print(help(archivo))
print(dir(archivo))

numeros1 = archivo.readline()
print(numeros1)
print(numeros1
      .split('\n'))
lista_num=[]
for linea in numeros1.split(','):
    for numero in linea.split(','):
        lista_num.append(int(numero))
print(lista_num)
lista_num.sort()
print(f"lista ordenada:{lista_num}")
print(f"El mayor es:{lista_num[-1]} y el menor es: {lista_num[0]}")
archivo.close()

archivo=open("numeros.txt","rt")
numeros2 = archivo.readlines()
print(numeros2)
archivo.close()

archivo=open("numeros.txt","rt")
numeros2 = archivo.readline()
print(numeros2)
archivo.close()

#tarea hacer lo mismo pero con readlines y quitarle los espacios
#hacer un banner con el nombre de la universidad en dorado, el de la fes en azul rey y el nombre de nosotros en verde claro

