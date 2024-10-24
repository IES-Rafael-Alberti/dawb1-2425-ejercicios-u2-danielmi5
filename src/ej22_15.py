#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
from mi_libreria import comprobar_entero
# guarda la suma en una variable "suma" y la retorna cuando se introduzca 0
def suma(entero):
    suma = 0
    while entero != 0:
        #A diferencia del código interior, si es negativo no se añade a la suma
        if entero > 0: 
            suma += entero
        entero = pedir_entero()
    return suma
        
# pide entero y retorna la variable comprobada si es un entero
def pedir_entero():
    entero = input("Introduce un entero ('0' para terminar): ").replace(" ","")
    return comprobar_entero(entero)
def main():
    entero = pedir_entero()
    print ("La sumatoria de todos los números positivos es:", suma(entero))
    
if __name__ == "__main__":
    main()