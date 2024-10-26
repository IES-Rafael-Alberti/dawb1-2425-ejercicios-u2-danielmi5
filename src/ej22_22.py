# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total
from mi_libreria import comprobar_entero
#comprueba si es positivo, si no bucle hasta q sí
def comprobar_positivo(num: str) -> int:
    if num < 0:
        while num < 0 :
            print ("**ERROR** => Debes introducir un número positivo")
            num = comprobar_entero(input("Introducir número entero positivo: "))
    return num
            
# pide el num y con las funciones comprobar por si hay algun error
def pedir_entero():
    entero = input("Introducir número entero positivo: ").replace(" ","")
    entero = comprobar_entero(entero)
    entero = comprobar_positivo(entero)
    if entero == 0:
        return None
    return entero

#Recorre el número digito a digito y por cada digito que sea se suma su contador. Retorna los contadores
def contar_pares_e_impares(num):
    contador_pares = 0
    contador_impares = 0
    for i in str(num):
        if int(i) % 2 == 0:
            contador_pares += 1
        else: 
            contador_impares += 1
    return contador_pares, contador_impares


    
    
def main():
    entero = pedir_entero()
    total_pares = 0
    total_impares = 0 
    # Repite pedir número hasta que este sea 0 (None), en cada bucle va a estar contando los pares e impares y en una variable vacía(total_..) el número total
    while entero is not None:
        pares, impares = contar_pares_e_impares(entero)
        
        #En caso de que sea uno, las palabras en singular (par, impar)
        if pares == 1 and impares == 1:
            print (f"Hay {pares} par y hay {impares} impar")
        elif pares == 1:
            print (f"Hay {pares} par y hay {impares} impares")
        elif impares == 1:
            print (f"Hay {pares} pares y hay {impares} impar")  
        else:
            print (f"Hay {pares} pares y hay {impares} impares")  
        
        total_pares += pares
        total_impares += impares
        entero = pedir_entero()
    print (f"Hay {total_pares} pares en total y hay {total_impares} impares en total") 
if __name__ == "__main__":
    main()