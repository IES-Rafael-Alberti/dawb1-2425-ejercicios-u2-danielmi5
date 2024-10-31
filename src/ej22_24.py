#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
from mi_libreria import comprobar_entero
import math


def pedir_entero():
    # pide el número y verifica si es un entero
    
    entero = input("Introduce un número entero (0 para terminar): ").replace(" ", "") # elimina espacios
    entero = comprobar_entero(entero)
    
    if entero == 0: # Si es 0
        return None  # Devuelve None para terminar el bucle en main
    else: # Si no retorna el entero
        return entero
        

# Comprueba si el número es primo, devuelve True si lo es y False si no lo es
def es_primo(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

def main():
    print("Introduce un número entero para verificar si es primo o no:")
    entero = pedir_entero()
    # contador para los primos
    contador = 0
    #mientras entero no sea 0 lo ejecuta
    while entero is not None:
        #si el número es primo, suma 1 al contador 
        if es_primo(entero):
            contador += 1
        # vuelve a pedir un entero
        entero = pedir_entero()
    
    print(f"Se han introducido {contador} números primos.")

if __name__ == "__main__":
    main()