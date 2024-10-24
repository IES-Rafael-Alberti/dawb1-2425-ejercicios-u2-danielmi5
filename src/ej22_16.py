#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

from mi_libreria import comprobar_entero
# guarda el número mayor en una variable "mayor" y la retorna cuando se introduzca 0
def comprueba_mayor(entero):
    mayor = entero
    while entero != 0:
        if entero > mayor: 
            mayor = entero
        entero = pedir_entero()
    return mayor

# comprueba si el entero leído es negativo
def comprobar_negativo(entero):
    while entero < 0 : 
        entero = input("Debes introducir un número entero positivo: ")
        entero = comprobar_entero(entero)
    return entero
        
# pide entero y retorna la variable comprobada si es un entero positivo
def pedir_entero():
    entero = input("Introduce un entero positivo ('0' para terminar): ").replace(" ","")
    return comprobar_negativo(comprobar_entero(entero))
def main():
    entero = pedir_entero()
    print (comprueba_mayor(entero), "es el número mayor.")
    
if __name__ == "__main__":
    main()