#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# Versión 2: Para impares y pares. Además con dos funciones más, una para comprobar si es par y la otra para crear fila
from mi_libreria import comprobar_entero

# pide el numero y lo devuelve
def pedir_entero():
    entero = input("").replace(" ","")
    return comprobar_num(comprobar_entero(entero))
# comprueba si el número es mayor a 0
def comprobar_num(entero):
    if entero <= 0 :
       while entero <=0:
           print("**ERROR** -> Introduce un número entero válida (>0):")
           entero = input("").replace(" ","")
           entero = comprobar_entero(entero)
    else:
        pass
    return entero
def es_par(entero: int) -> bool:
    if entero % 2 == 0:
        return True
    else: 
        return False

def crear_triangulo(entero):
    triangulo =  ""
    if es_par(entero):
        # recorre todos los numeros impares desde el 2 hasta el numero impuesto
        for i in range (2, entero +1, 2):
            # añade al triangulo la fila y un salto de linea
            triangulo += crear_fila(entero, i) + "\n"
    else: 
        # recorre todos los numeros impares desde el 1 hasta el numero impuesto
        for i in range (1, entero +1, 2):
           # añade al triangulo la fila y un salto de linea
            triangulo += crear_fila(entero, i) + "\n"
    return triangulo

def crear_fila(entero, inicio):
    fila = ""
    if es_par(entero): 
        #Recorre el numero actual (más alto) de la fila hasta 0 (sin añadir este) de dos en dos
        for i in range (inicio, -2, -2):
            # Por cada fila me imprime cada numero i del for, desde el numero actual (inicio) hasta 0 (sin añadir este), creando un espacio entre ellos.
            if i != 2:
                fila += str(i) + " "
            else: # Si es 2 imprime el último número ("sin espacio") y retorna la fila
                fila += str(i)
                return fila
    else: # Si es impar
        # Recorre el numero actual (inicio) (más alto) de la fila hasta 1 de dos en dos
        for i in range (inicio, -1, -2):
                # Por cada fila me imprime cada numero i del for, desde el numero actual hasta uno, creando un espacio entre ellos.
                if i != 1:
                    fila += str(i) + " "
                else: #Cuando llegue al 1 no imprime el espacio
                    fila += str(i)
    return fila 
    
        
def main():
    print("Introduce el número entero del triangulo:", end=" ")
    numero = pedir_entero()
    triangulo = crear_triangulo(numero)
    print (triangulo)
if __name__ == "__main__":
    main()