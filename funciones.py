def sumar( x , y ):
    z = x + y
    return z

def restar (x ,  y):
    return x - y

def main ():
    a = 10
    b = 5
    c = sumar(a,b)
    print(f"la suma de esto {a} y {b} es {c}")
    c = restar(a,b)
    print(f"la resta de esto {a} y {b} es {c}")

    
if  __name__ == '__main__':  #¿Se mandó a ejecutar (interpretar) este archivo?  
    main()


#otro sin main
def sumar( x , y ):
    z = x + y
    return z

def restar (x ,  y):
    return x - y
a = 10
b = 5
c = sumar(a,b)
print(f"la suma de esto {a} y {b} es {c}")
c = restar(a,b)
print(f"la resta de esto {a} y {b} es {c}")

# otra funcion
def sumar( x , y ):
    z = x + y
    return z
def restar (x ,  y):
    return x - y

def mi_print(texto):
    print(f"Este es mi print: {texto}")

def multiplica(valor , veces):
    if veces == None:
        print("Debes enviar el segundo argumento de la funcion ")
    else:
        print(valor * veces)

def comanda( mesa , comensal , entrada , medio , fuerte , postre ="Gela de limon"):
    print(f"\t Mesa: {mesa} comensal:{comensal}")
    print(f"\t Entrada: {entrada} ")
    print(f"\t Segundo tiempo: {medio}")
    print(f"\t Plato fuerte: {fuerte}")
    print(f"\t Postre: {postre}")

def comanda2(**comida):
    llaves = comida.keys()
    for elem in llaves:
        print("->",comida[elem])

def imprime_argumentos(*argumentos):
    #print('---->',argumentos,'<----')
    #for ele in argumentos:
    for index in range(len(argumentos) ):
        #print(ele)
        print(argumentos[index] )


mi_print("Hola!!")
multiplica(10 , 3)
multiplica(10 , None)
multiplica('Hola'  , 3)
comanda(2,1,"Ensalada","sopa de rana","filete de pompi de sirena", "Flan")
comanda("Ensalada","sopa de rana","filete de pompi de sirena", "Flan",2,1)
comanda(entrada="Ensalada",medio="sopa de rana",fuerte="filete de pompi de sirena",mesa=2,comensal=1)
imprime_argumentos('Hola',True,3.1416, 1000, {'ID':'sc01', 'nombre':'juan'})
imprime_argumentos()
comanda2(entrada="Ensalada",medio="sopa de rana",fuerte="filete de pompi de sirena",mesa=2,comensal=1,postre="Strudel de manzana", bebida='coca light')


