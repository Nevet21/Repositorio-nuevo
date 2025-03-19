##creo la lista donde estaran guardadas las palabras en ingles#
import os
import random
listaP=[]
if not os.path.exists("Palabras.txt"):
    with open("Palabras.txt","w", encoding="utf-8") as archivo:
        pass


def cargarPalabras(listaP):
    with open("Palabras.txt","r", encoding="utf-8") as archivo:
        for linea in archivo:
            listaP.append(linea.strip())
        archivo.close()
    print(listaP)
    

def agregarPalabras(listaP):

    ok=True
    palabraI=""
    palabraE=""
    num=int(0)
    print("Ingrese las palabra en español seguido de su significado en ingles, para  salir escriba terminar ")
    while ok:
            palabraE=input("ingrese la palabra en español: ")
            if palabraE==("terminar"):
                ok=False
            else:
                palabraI=input("ingrese la palabra en ingles: ")
                listaP.append(palabraE)
                listaP.append(palabraI)
                listaP.append(int(0))
                with open("Palabras.txt","a", encoding="utf-8") as archivo:
                    archivo.write(palabraE+"\n")
                    archivo.write(palabraI+"\n")
                    archivo.write("0"+"\n")
                    archivo.close()

    
    return listaP
            
            
def buscarPalabra(listaP):
    palabraB=input("ingrese la palabra que requiere la traduccion: ")
    significado=""
    x=0
    while x<len(listaP):
        if palabraB==listaP[x]:
            if listaP.index(palabraB)%3==0:
                significado=listaP[x+1]
            else:
                if listaP.index(palabraB)%3!=0:
                    significado=listaP[x-1]
                else:
                    print("la palabra no se encuentra en el diccionario ")
        x=x+1
    
    print("traduccion: "+str(significado))
    
    
def EditarPalabra(listaP):
    ok=True
    EdPalabra=input("ingrese la palabra que desea editar: ")
    while ok:
        try:
            indexP=int(listaP.index(EdPalabra))
            ok=False
        except ValueError:
            print("la palabra buscada no se encuentra en el diccionario, ingrese otra nuevamente  ")
            salir=input("si desea salir ingrese false ")
            if salir=="false":
                ok=False
    listaP[indexP]=input("ingrese la edicion a la palabra: ")
    if indexP%3==0:
        listaP[indexP+1]=input("ingrese el nuevo significado: ")
    else:
        listaP[indexP-1]=input("ingrese su nuevo significado: ")

    print("Se edito correctamente")
    
    with open("Palabras.txt","w", encoding="utf-8") as archivo:
        for elemento in listaP:
            archivo.write(str(elemento)+"\n")
        archivo.close()
    

def EliminarPalabra(listaP,EliPalabra):
    if EliPalabra=="":
        EliPalabra=input("ingrese la palabra que desea eliminar: ")
    indexP=int(listaP.index(EliPalabra))
    
    try:
        indexP=int(listaP.index(EliPalabra))
    except IndexError:
        print("la palabra buscada no se encuentra en el diccionario, ingrese otra nuevamente  ")

    print(listaP)
    print(indexP)
    
    if indexP%3==0:
        del listaP[indexP+2]
        del listaP[indexP+1]
        del listaP[indexP]
    else:
        del listaP[indexP]
        del listaP[indexP-1]
        del listaP[indexP-2]
    print("Se elimino correctamente ")
    print(listaP)
    
    with open("Palabras.txt","w", encoding="utf-8") as archivo:
        for elemento in listaP:
            archivo.write(str(elemento)+"\n")
        archivo.close()

def evaluacionEspañol(listaP):
    traduccion=""
    num=1
    contador=0
    print("Bienvenido al modo evaluacion ")
    print("A continuacion se le preguntaran 5 palabras en español a las cuales debera dar su traduccion en ingles:  ")
    for x in range(0,5):
        while num%3!=0:
            num=random.randint(0,(len(listaP)-1))
        print(num)
        print(len(listaP))
        traduccion=input("ingrese la traduccion de "+ str(listaP[num])+" :")
        if traduccion==listaP[num+1]:
            contador=int(listaP[num+2])
            contador=contador+1
            listaP[num+2]=contador
            print("Correcto "+"\u2714")
        else:
            contador=0
            listaP[num+2]=0
            print("incorrecto "+"\u2716")
        if listaP[num+2]==5:
            EliminarPalabra(listaP,listaP[num])
        num=1
    with open("Palabras.txt","w", encoding="utf-8") as archivo:
        for elemento in listaP:
            archivo.write(str(elemento)+"\n")
        archivo.close()
    

##llamados de las funciones
if len(listaP)==0:
    cargarPalabras(listaP)
EliminarPalabra(listaP)


