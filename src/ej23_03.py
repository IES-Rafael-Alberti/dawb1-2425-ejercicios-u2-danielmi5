#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.
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
                print ("**ERROR** -> Valor incorrecto (Número negativo)")
                num = None
    return num

def comprobar_positivo(num):
    if num < 0:
        raise ValueError ("**ERROR** -> Número negativo introducido (Fuera del rango): ", num)
    
# obtiene la cadena de todos los números desde num hasta 0  
def obtener_cuenta_atras(num):
    # cadena vacía para guardar la cuenta atras
    cuenta_atras = ""
    # recorre desde el número hasta 0
    for i in range(num, -1, -1):
        # si i es 0, i es el último número, por lo que detrás en vez de una coma añado un punto
        if i == 0:
            cuenta_atras += str(i) + "."
        else: #De lo contrario, añade el número con coma
            cuenta_atras += str(i) +", "
       
    #retorna la cadena 
    return cuenta_atras
    
    
def main():
    num = pedir_numero()
    cuenta_atras = obtener_cuenta_atras(num)
    print (f"Cuenta atras desde {num}: \n",cuenta_atras)
if __name__ == "__main__":
    main()