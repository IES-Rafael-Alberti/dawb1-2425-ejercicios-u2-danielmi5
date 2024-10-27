#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
def pedir_numero():
    num = None
    while num is None:
        try:
            num = int(input("Introduce un número entero positivo: "))
            comprobar_positivo(num)
        # si falla la conversión salta la excepción ValueError
        except ValueError:
            #Si es None es porque ha saltado error por la conversión
            if num is None:
                print ("**ERROR** -> Debes introducir un número entero")
            # De lo contrario es porque ha saltado error en comprobar_positivo
            else:
                print ("**ERROR** -> Valor incorrecto (Fuera del rango, es <1)")
                # num vuelve a valer None para que vuelva a pedir un número
                num = None
    return num
                
def comprobar_positivo(num):
    # si num es menos a 1 salta el error
    if num < 1:
        raise ValueError ("**ERROR** -> Número incorrecto introducido (Fuera del rango, es <1): ", num)
# Si es impar retorna True, si no retorna False
def es_impar(num):
    if num % 2 != 0:
        return True
    else: 
        return False

# obtiene la cadena de todos los impares desde 1 hasta ese número   
def obtener_impares(num):
    # cadena vacía para guardar los impares
    cadena_impares = ""
    # recorre desde 1 hasta el numero, si i es impar lo añade a la cadena.
    for i in range(1, num + 1):
        if es_impar(i):
            # si es mayor o igual, i es el último número, por lo que detrás en vez de una coma añado un punto
            if i >= num-1:
                cadena_impares += str(i) + "."
            else: #De lo contrario, añade el número con coma
                cadena_impares += str(i) +", "
        else: #Si no lo es, no hace nada.
            pass
    #retorna la cadena 
    return cadena_impares
        
    

    

def main():
    num = pedir_numero()
    cadena_impares = obtener_impares(num)
    print (f"Los números impares desde 1 hasta {num} son: \n",cadena_impares)
    
if __name__ == "__main__":
    main()