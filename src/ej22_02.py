#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
from mi_libreria import comprobar_entero
      
def pedir_edad():
    edad = input("").replace(" ","")
    return comprobar_edad(comprobar_entero(edad))

def comprobar_edad(edad):
    if edad <= 0 or edad > 125:
       while edad <= 0 or edad > 125:
           print("**ERROR** -> Introduce una edad válida:")
           edad = input("").replace(" ","")
           edad = comprobar_entero(edad)
    else:
        pass
    return edad
def mostrar_anios(edad):
    for i in range(1,edad+1):
            if i == edad:
                print (i)
            else:    
                print (i, end ="-")

def main():
    print ("¿Cuál es tu edad?")
    edad = pedir_edad()
    mostrar_anios(edad)
if __name__ == "__main__":
    main()