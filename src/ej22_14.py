#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
from mi_libreria import comprobar_entero
def suma(entero):
    suma = 0
    while entero != 0:
        suma += entero
        entero = pedir_entero()
    return suma
        
    
def terminar_programa(entero):
    if entero == 0:
        return True
    else: 
        return False

def pedir_entero():
    entero = input("Introduce un entero ('0' para terminar): ").replace(" ","")
    return comprobar_entero(entero)
def main():
    entero = pedir_entero()
    print ("La sumatoria es:", suma(entero))
    
if __name__ == "__main__":
    main()