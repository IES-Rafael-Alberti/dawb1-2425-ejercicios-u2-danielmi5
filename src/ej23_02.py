#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
def pedir_numero():
    num = None
    while num is None:
        try:
            num = int(input("Introduce un número entero positivo: "))
            comprobar_positivo(num)
        except ValueError:
            if num is None:
                print ("**ERROR** -> Debes introducir un número entero")
            else:
                print ("**ERROR** -> Valor incorrecto (Fuera del rango, es <1)")
                num = None
    return num
                
def comprobar_positivo(num):
    if num < 1:
        raise ValueError ("**ERROR** -> Número incorrecto introducido (Fuera del rango, es <1): ", num)
    
def es_impar(num):
    if num % 2 != 0:
        return True
    else: 
        return False
    
def obtener_impares(num):
    cadena_impares = ""
    for i in range(1, num + 1):
        if es_impar(i):
            if i >= num - 3:
                if i < num-1:
                    cadena_impares += str(i) + " y "
                else: 
                    cadena_impares += str(i) + "."
                
            else:
                cadena_impares += str(i) +", "
        else:
            pass
    return cadena_impares
        
    

    

def main():
    num = pedir_numero()
    cadena_impares = obtener_impares(num)
    print (f"Los números impares desde 1 hasta {num} son: \n",cadena_impares)
    
if __name__ == "__main__":
    main()