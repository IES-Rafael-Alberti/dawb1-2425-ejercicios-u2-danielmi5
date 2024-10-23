#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
from mi_libreria import comprobar_entero
import math

def pedir_entero():
    entero = input("").replace(" ","") #elimino espacios
    return comprobar_entero(entero)

# comprueba si el número ea primo, devuelve True si lo es y False si no lo es
def es_primo(entero: int) -> bool:
    if entero < 2:
        return False
    elif entero == 2:
        return True  
    elif entero != 2 and entero % 2 == 0:
        return False
    else:
        terminar = False
        for i in range(3, int(math.sqrt(entero)) + 1, 2):
            if entero % i == 0:
                terminar = True
                return False
        if terminar == False:
            return True
    
         

def main():
    print("Introduce un número entero:", end=" ")
    numero = pedir_entero()
    if es_primo(numero):
        print(numero,"es primo.")
    else:
        print(numero,"no es primo.")
    
if __name__ == "__main__":
    main()

