#optimización de la función frente al ej21_03 (añadido mejor manera de comprobar negativo y soporte para decimales con funcion es_decimal)
def comprobar_num(num: str):
    if num.isdigit():
        return int(num)
    else: # Si entra un numero negativo, como tiene guion lo detecta como si no fuese digito, pasa lo mismo con decimales
        while not num.isdigit():
            #compruebo si es negativo
            if num.startswith("-"):
                # si a partir del guion es digit, eso significa que es negativo.
                if num[1:].isdigit():
                    return int(num)
                # de lo contrario si es negativo y decimal             
                elif es_decimal(num[1:]):
                    return float(num)
                else:
                    pass
            #compruebo si es decimal
            if es_decimal(num):
                return float(num)
            else:
                pass
                    
            print("ERROR: Debes introducir un número: ")
            num = input("").replace(" ","")
    
    return int(num)

def es_decimal(num: str) -> bool:
    # si tiene mas de un punto es una cadena
    if num.count(".") > 1:
        return False
    else: #puede ser decimal
        if num.replace(".","").isdigit():
            return True
        else: 
            return False