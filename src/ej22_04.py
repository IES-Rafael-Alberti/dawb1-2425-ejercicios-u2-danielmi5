#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
from mi_libreria import comprobar_entero
# replace elimino espacios      
def pedir_entero():
    entero = input("").replace(" ","")
    return comprobar_positivo(comprobar_entero(entero))
# comprueba si es positivo, si no lo es, bucle hasta q sí. Al final retorna el número.
def comprobar_positivo(entero):
    if entero < 0 :
       while entero <0:
           print("**ERROR** -> Introduce un número positivo :" , end=" ")
           entero = input("").replace(" ","")
           entero = comprobar_entero(entero)

    return entero
# Añade en una cadena la cuenta atrás del número y retorna la cuenta atrás
def obtener_cuentra_atras(entero):
    cuenta_atras = ""
    #recorre desde el número hasta 0
    for i in range(entero,0 - 1, -1):
            if i == 0: # si es el último num de la cuenta, añade un punto al final
                cuenta_atras += str(i) + "."
            else: # Si no añade coma   
                cuenta_atras += str(i) + ", "
    return cuenta_atras
def main():
    print ("Introduce un número entero positivo:",end=" ")
    entero = pedir_entero()
    cuenta_atras= obtener_cuentra_atras(entero)
    print (cuenta_atras)
if __name__ == "__main__":
    main()
