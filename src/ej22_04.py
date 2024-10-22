#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
from mi_libreria import comprobar_entero
      
def pedir_entero():
    entero = input("").replace(" ","")
    return comprobar_positivo(comprobar_entero(entero))

def comprobar_positivo(entero):
    if entero < 0 :
       while entero <0:
           print("**ERROR** -> Introduce un número positivo :" , end=" ")
           entero = input("").replace(" ","")
           entero = comprobar_entero(entero)
    else:
        pass
    return entero
def mostrar_cuentra_atras(entero):
    for i in range(entero,0 - 1, -1):
            if i == 0:
                print (i)
            else:    
                print (i, end =", ")

def main():
    print ("Introduce un número entero positivo:",end=" ")
    entero = pedir_entero()
    mostrar_cuentra_atras(entero)
if __name__ == "__main__":
    main()
