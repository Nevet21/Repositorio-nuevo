listaMenu = []

def cargarPalabras(listaP):
    with open("menu.txt","r", encoding="utf-8") as archivo:
        for linea in archivo:
            listaMenu.append(linea.strip())
        archivo.close()
    print(listaP)
    
def agregarPlato(listaMenu):
    plato = input("Ingrese el plato que se desea agregar:  ")
    precio =  (input("Ingrese el precio del plato:  "))
    listaMenu.append(plato)
    listaMenu.append(precio)
    
    with open ("menu.txt", "a", encoding="utf-8") as archivo:
        archivo.write(plato+"\n")
        archivo.write(precio+"\n")
        archivo.close()
        
def buscarPlato(listaMenu):

        buscarPlato = input("Ingrese el plato que desea buscar: ")
        x=0
        while x<len(listaMenu):
                if listaMenu[x]==buscarPlato:
                    precio=listaMenu[x+1]
        print("El precio para el plato buscado es: " + precio)
        
def buscarActualizarEliminarPlato(listaMenu,actualizarPlato):
    x=0
        
    while x<len(listaMenu):
            if listaMenu[x]==buscarPlato:
                precio=listaMenu[x+1]
            x=x+1
    return x
        
def actualizarPlato(listaMenu):
    platoAct = input("¿Que plato desea actuaklizar?")
    x = buscarActualizarEliminarPlato(listaMenu,platoAct)
    listaMenu[x] = input("Ingrese el nuevo plato: ")
    listaMenu[x+1] = (input("Ingrese el nuevo precio"))
    
    with open ("menu.txt", "w", encoding="utf-8") as archivo:
        for linea in archivo:
            listaMenu.append(linea.strip())
        archivo.close()
        
def eliminarPlato(listaMenu):
    eliminarPlato = input("Ingrese el plato a eliminar")
    
    x = buscarActualizarEliminarPlato(listaMenu,eliminarPlato)
    print(listaMenu)
    print(x)
    del listaMenu[x-1]
    del listaMenu[x-2]
    
    with open ("menu.txt", "w", encoding="utf-8") as archivo:
        for linea in listaMenu:
            listaMenu.append(linea.strip())
        archivo.close()
        
agregarPlato(listaMenu)
cargarPalabras(listaMenu)
eliminarPlato(listaMenu)
  
    
    
    

    
        
                
            
