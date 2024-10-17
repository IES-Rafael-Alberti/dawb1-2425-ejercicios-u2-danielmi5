#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def comprobar_num(num: str) -> int:
    if num.isdigit():
        return int(num)
    else:
        while not num.isdigit():
            print("ERROR: Debes introducir un número: ")
            num = input("").replace(" ","")
        return int(num)

def comprobar_Par(num):
    if (num%2 == 0):
        print("Es par")
    else:
        print ("Es impar")

def main():
    num = input("Introduce un número: ").replace(" ","")
    num = comprobar_num(num)
    comprobar_Par(num)
    
if __name__ == "__main__":
    main()