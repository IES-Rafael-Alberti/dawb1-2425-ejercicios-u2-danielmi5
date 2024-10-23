#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
def pedir_cadena():
    cadena = input("").replace(" ")
    return cadena

def mostrar_eco(cadena):
    # variable vacía
    eco = ""
    # variable para terminar bucle
    terminar = False
    # Mientras no salga salir lo ejecuta
    while not terminar == True:
        #A la variable vacía se le añade cada palabra con un espacio
        eco += cadena + " "
        print(eco)
        cadena = input("Introduce otra cadena ('salir' para terminar): ").replace(" ","")
        # cuando salga salir termina
        terminar = terminar_programa(cadena)
        
def terminar_programa(cadena: str) -> bool:
    if cadena.lower() == "salir":
        return True
    else:
        return False

def main():
    print ("Introduce una cadena:")
    cadena = pedir_cadena()
    mostrar_eco(cadena)
if __name__ == "__main__":
    main()