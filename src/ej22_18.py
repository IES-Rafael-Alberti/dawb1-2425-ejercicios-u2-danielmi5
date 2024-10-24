#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
from mi_libreria import comprobar_entero
# guarda la suma en una variable "suma" y la retorna cuando se introduzca -1
def suma_digito(entero: int) -> int:
    pares = ""
    while entero != -1 :
        suma = 0
        pares = guarda_pares(entero, pares)
        #le asigno entre 0 y la longitud del número (como no funciona con int lo conviero a str)
        for i in range (0,len(str(entero))):
            suma += int(str(entero)[i])
        print (f"La suma de todos los dígitos de {entero} es:",suma)
        entero = pedir_entero()
    
    return str(pares)

def guarda_pares(entero: int, pares: int) -> bool:
    if entero % 2 == 0:
        entero = str(entero) + ", "
        pares += entero
    return pares
        
# pide entero y retorna la variable comprobada si es un entero
def pedir_entero():
    entero = input("Introduce un número ('-1' para terminar): ").replace(" ","")
    return comprobar_entero(entero)
def main():
    entero = pedir_entero()
    pares = suma_digito(entero)
    print ("Los pares son: ",pares)
    
if __name__ == "__main__":
    main()