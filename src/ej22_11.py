#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
def invertir_cadena(cadena: str):
    #recorre la cadena desde el final imprimiendo letra por letra
    for i in cadena[::-1]:
        print (i)

#pide una cadena
def pedir_cadena():
    cadena = input("").replace(" ","")
    return cadena

def main():
    print("Introduce una palabra:", end=" ")
    cadena = pedir_cadena()
    invertir_cadena(cadena)
    
    
if __name__ == "__main__":
    main()