#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
from mi_libreria import comprobar_entero

# pide el numero y lo devuelve
def pedir_entero():
    entero = input("").replace(" ","")
    return comprobar_num(comprobar_entero(entero))
# comprueba si el número es mayor a 0
def comprobar_num(entero):
    if entero <= 0 :
       while entero <=0:
           print("**ERROR** -> Introduce una altura válida:")
           entero = input("").replace(" ","")
           entero = comprobar_entero(entero)
    else:
        pass
    return entero

def crear_triangulo(altura):
    # recorre todos los numeros impares desde el 1 hasta el numero impuesto
    for i in range (1, altura +1, 2):
        # Recorre el numero actual (más alto) de la fila hasta 1 de dos en dos
        for i in range (i, -1, -2):
            # Por cada fila me imprime cada numero i del for, desde el numero actual hasta uno, creando un espacio entre ellos. 
            if i != 1:
                print(i, end= " ")
            else: #Cuando llegue al 1 no imprime el espacio
                print(i)
            
        
def main():
    print("Introduce la altura del triangulo:", end=" ")
    altura = pedir_entero()
    crear_triangulo(altura)
if __name__ == "__main__":
    main()