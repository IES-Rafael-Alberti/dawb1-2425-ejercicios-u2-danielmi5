#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
from mi_libreria import comprobar_entero
      
def pedir_entero():
    entero = input("").replace(" ","")
    return comprobar_positivo(comprobar_entero(entero))

def comprobar_positivo(entero):
    if entero < 0 :
       while entero <0:
           print("**ERROR** -> Introduce un número positivo :")
           entero = input("").replace(" ","")
           entero = comprobar_entero(entero)
    else:
        pass
    return entero
# guarda todos los impares desde el número dado hasta 1 y los guarda en una variable impares
def obtener_impares(entero: int) -> str:
    impares = ""
    # recorre todos los números hasta 1
    for i in range(1,entero+1):
        # Si es par no hace nada y continua
        if i % 2 == 0:
            continue
        else: # Si es impar los añade a la variable impares
            if i == entero: #Si el número es el dado, lo añade, pero sin coma
                impares += (str(i))
            else: # Si es otro número, lo añade con coma   
                impares += str(i) + ", "
    return impares


def main():
    print ("Introduce un número entero positivo:")
    entero = pedir_entero()
    impares = obtener_impares(entero)
    print("Todos los impares desde el número hasta 1:",impares)
if __name__ == "__main__":
    main()
