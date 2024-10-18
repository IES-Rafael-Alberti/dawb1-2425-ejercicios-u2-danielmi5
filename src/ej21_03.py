#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
def comprobar_num(num: str) -> int:
    if num.isdigit():
        return int(num)
    else:
        while not num.isdigit():
            if num.startswith("-"):
                num = num.replace("-","",1)
                if num.isdigit():
                    num = "-" + num
                    return int(num)
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