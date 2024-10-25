#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
from mi_libreria import comprobar_entero
def pedir_entero():
    entero = input("").replace(" ","")
    return comprobar_positivo(comprobar_entero(entero))
# comprueba si la altura es positivo, si no bucle hasta que sí.
def comprobar_positivo(entero):
    if entero < 0 :
       while entero <0:
           print("**ERROR** -> Introduce una altura válida:")
           entero = input("").replace(" ","")
           entero = comprobar_entero(entero)
    else:
        pass
    return entero

def main():
    print("Introduce la altura del triangulo:", end=" ")
    altura = pedir_entero()
    # recorre desde 1 hasta la altura dada
    for i in range (1, altura +1):
        # imprime el '*' el número de veces de i (fila 1 un *, fila 2  dos *, fila 3  tres *...)
        print (("*")*i)
if __name__ == "__main__":
    main()
