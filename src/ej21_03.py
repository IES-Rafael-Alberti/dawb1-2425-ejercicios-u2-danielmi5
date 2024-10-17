#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
def comprobar_num(num: str) -> int:
    if num.isdigit():
        return int(num)
    else:
        while not num.isdigit():
            print("ERROR: Debes introducir un número: ")
            num = input("").replace(" ","")
        return int(num)

def comprobar_division(num1: int, num2: int) -> float:
    if num2 == 0:
        
        return "*ERROR* --> No se puede dividir por 0"
    else: 
        division = num1 / num2
        return float(division)

def main():
    num1 = input("Introduce un número: ").replace(" ","")
    num2 = input("Introduce un número: ").replace(" ","")
    num1 = comprobar_num(num1)
    num2 = comprobar_num(num2)
    resultado = comprobar_division(num1, num2)
    print( num1, " / ", num2, " = ", resultado)
if __name__ == "__main__":
    main()