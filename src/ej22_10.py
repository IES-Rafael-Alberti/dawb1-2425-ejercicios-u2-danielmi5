#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
from mi_libreria import comprobar_entero

def pedir_entero():
    entero = input("").replace(" ","")
    return comprobar_entero(entero)

# comprueba si el número es mayor a 0
def comprobar_primo(entero: int) -> bool:
    if entero < 0 :
       while entero <=0:
           print("**ERROR** -> Introduce una altura válida:")
           entero = input("")
           entero = comprobar_entero(entero)
    else:
        pass
    return entero

def main():
    print("Introduce un número entero:")
    
if __name__ == "__main__":
    main()

