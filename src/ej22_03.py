#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
from mi_libreria import comprobar_entero
      
def pedir_entero():
    entero = input("")
    return comprobar_positivo(comprobar_entero(entero))

def comprobar_positivo(entero):
    if entero < 0 :
       while entero <0:
           print("**ERROR** -> Introduce un número positivo :")
           entero = input("")
           entero = comprobar_entero(entero)
    else:
        pass
    return entero
def mostrar_impares(entero):
    for i in range(1,entero+1,2):
            if i == entero:
                print (i)
            else:    
                print (i, end =", ")

def main():
    print ("Introduce un número entero positivo")
    entero = pedir_entero()
    mostrar_impares(entero)
if __name__ == "__main__":
    main()
