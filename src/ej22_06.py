#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
from mi_libreria import comprobar_entero
def pedir_entero():
    entero = input("").replace(" ","")
    return comprobar_positivo(comprobar_entero(entero))
def comprobar_positivo(entero):
    if entero < 0 :
       while entero <0:
           print("**ERROR** -> Introduce una altura válida:")
           entero = input("").replace(" ","")
           entero = comprobar_entero(entero)
    else:
        pass
    return entero
def crear_triangulo(altura):
    for i in range (1, altura +1):
        print (("*")*i)
def main():
    print("Introduce la altura del triangulo:", end=" ")
    altura = pedir_entero()
    crear_triangulo(altura)
if __name__ == "__main__":
    main()
