#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

def pedir_frase():
    frase = input("Introduzca una frase: ").strip() # elimino los espacios antes y despues de la frase
    return frase

def comprobar_letra(letra: str) -> str:
    letra = letra.lower()
    #compruebo si letra es una letra, si no bucle hasta que sí
    while len(letra) != 1 or (not letra >= "a" and letra <= "z"):
        print ("**ERROR** -> caracter no válido")
        letra = input("Introduce una LETRA: ").replace(" ","") # elimino espacios
    return letra    
    
def pedir_letra():
    letra = input("Introduce una letra: ").replace(" ","") # elimino espacios
    return comprobar_letra(letra)

def main():
    frase = pedir_frase()
    letra = pedir_letra()
    posicion = 0
    # recorre la frase comprobando letra por letra. Y por cada letra se aumenta la variable posición para que coincida con la posición de la letra
    for i in frase:
        posicion += 1
        # como letra va ser minúscula, añado lower a i para que coincida (Ya que existe la posibilidad que i sea mayúscula)
        if i.lower() != letra:
            print(f"No hay coincidencia en la posición {posicion}")
        else:
            print(f"Hay coincidencia en la posición {posicion}")
            break # termina el código
    
if __name__ == "__main__":
    main()