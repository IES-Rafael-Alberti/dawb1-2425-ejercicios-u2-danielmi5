#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
def invertir_cadena(cadena: str) -> str:
    #recorre la cadena desde el final letra por letra, invirtiendola
    cadena_invertida = cadena[::-1]
    return cadena_invertida
    

#pide una cadena
def pedir_cadena():
    cadena = input("").replace(" ","")
    return cadena

def main():
    print("Introduce una palabra:", end=" ")
    cadena = pedir_cadena()
    cadena_invertida = invertir_cadena(cadena)
    print (cadena_invertida)
    
    
if __name__ == "__main__":
    main()