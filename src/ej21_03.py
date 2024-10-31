#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
def es_decimal(num: str) -> bool:
    # si tiene mas de un punto es una cadena, por lo que retorna False
    if num.count(".") > 1 or num.count(".") == 0:
        return False
   
    else: #puede ser decimal
        if num.replace(".","").isdigit():
            return True
        else: 
            return False

def comprobar_num(num: str):
    if num.isdigit():
        return int(num)
    else: # Si entra un numero negativo, como tiene guion lo detecta como si no fuese digito, pasa lo mismo con decimales
        while not num.isdigit():
            #compruebo si es decimal
            if es_decimal(num):
                return float(num)
            else:
                pass
            # Compruebo si es un numero negativo
            if num.startswith("-"):
                num = num.replace("-","",1)
                if num.isdigit():
                    num = "-" + num
                    return int(num)
                # compruebo si puede llegar a ser negativo y decimal
                if es_decimal(num):
                    return float(num)
                else: 
                    pass
                
           
            # Si no es todo lo anterior es una cadena
            print("ERROR: Debes introducir un número: ")
            num = input("").replace(" ","")
    return int(num)

def comprobar_division(num: int, divisor: int) -> float:
    if divisor == 0:
        
        return "*ERROR* --> No se puede dividir por 0"
    else: 
        division = num / divisor
        return float(division)
        

def main():
    num = input("Introduce un número: ").replace(" ","")
    num = comprobar_num(num)
    divisor = input("Introduce un número: ").replace(" ","")
    divisor = comprobar_num(divisor)
    
    resultado = comprobar_division(num, divisor)
    print( num, " / ", divisor, " = ", resultado)
if __name__ == "__main__":
    main()