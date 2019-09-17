#print tiene 4 formas de uso
"""
1.- Con comas
2.- con signo '+'
3.- con la funcion format()
4.- es con una variante de format()
"""
#Con comas , concatenar agregando
# un espacio y haciendo casting de tipo
edad = 10
nombre = "Juan"
estatura =1.67
print(edad , estatura , nombre)
#Con '+' hace lo mismo pero no hace el casting automático
#No agrega espacio
print(str(edad) + str(estatura) + nombre)

#funcion format()
print("Nombre:{} Edad:{} Estatura:.{}".format(nombre,edad,estatura))

#4.-con una variante de format() simplificada
print(f"Nombe: \"{nombre}\" \nEdad:\t{edad} ")

#print y el argumento end
print("Solo hay dos tipos de personas, las que saben binario y las que no",end=" ")
print("otra linea")
 
