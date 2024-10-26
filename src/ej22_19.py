#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

# input opcion
def elegir_opcion():
    opcion = input ("Introduce una opción (1, 2 o 3): ").replace(" ","")
    return comprobar_opcion(opcion)
#comprueba si la opcion es 1, 2 o 3, si no bucle hasta que sí
def comprobar_opcion(opcion):
    valida = False
    while valida == False:
        if opcion == "1":
            valida = True
        elif opcion == "2":
            valida = True
        elif opcion == "3":
            valida = True
        else: 
            print ("**ERROR** -> Opción no válida")
            opcion = input("Debes introducir una opción válida (1, 2 o 3): ").replace(" ","")
    return opcion

def main():
    menu = "Este es el menú:\n1: Comenzar programa\n2: Imprimir listado\n3: Finalizar programa"
    seguir = True
    # mientras la opcion sea 1 o 2 vuele a pedir otra opcion, si es 3 termina
    while seguir == True:
        print(menu)
        print("") #Para que no se vea tan pegado el menú con elegir_opcion (salto de linea))
        opcion = elegir_opcion()
        if opcion == "1" or opcion == "2":
            if opcion == "1":
                print("Comenzando programa...")
            else:
                print("Imprimiendo listado...") 
            print("") #Para que no se vea tan pegado el menú con el texto impreso (salto de linea)
        else:
            print ("Finalizando programa...")
            seguir = False
if __name__ == "__main__":
    main()