#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
from mi_libreria import comprobar_entero
# guarda la suma total de los dígitos en una variable "suma" y la retorna cuando termine el bucle for.
def suma_digito(entero):
    suma = 0
    #le asigno entre 0 y la longitud de número
    for i in range (0,len(str(entero))):
        # va sumando a una variable (suma = 0) cada dígito
        suma += int(str(entero)[i])
    return suma


# comprueba si el entero leído es negativo, si no bucle hasta que sí. Al final retorna el número
def comprobar_negativo(entero):
    while entero < 0 : 
        entero = input("Debes introducir un número entero positivo: ")
        entero = comprobar_entero(entero)
    return entero
        
# pide entero y retorna la variable comprobada si es un entero positivo
def pedir_entero():
    entero = input("Introduce un número entero positivo: ").replace(" ","")
    return comprobar_negativo(comprobar_entero(entero))

def main():
    entero = pedir_entero()
    print (suma_digito(entero), "es la suma total de los digitos.")
    
if __name__ == "__main__":
    main()
