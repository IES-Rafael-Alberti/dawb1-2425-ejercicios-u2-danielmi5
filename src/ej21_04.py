#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
from mi_libreria import comprobar_num
#Si es par retorna True, si no False
def comprobar_Par(num):
    if (num%2 == 0): 
        return True
    else:
        return False

def main():
    num = input("Introduce un número: ").replace(" ","")
    num = comprobar_num(num)
    if comprobar_Par(num): #Si es par
        print ("Es par")
    else: # Si no es par
        print ("Es impar")
    
if __name__ == "__main__":
    main()