#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
#compruebo si la letra es solamente una letra y si es una letra (Con el respectivo bucle para que vuelva a pedir)
def comprobar_letra(letra: str) -> str:
    while len(letra) != 1 or (not letra >= "a" and letra <= "z"):
        letra = input("Introduce una LETRA: ").replace(" ","")
    return letra    

def pedir_letra():
    letra = input("").replace(" ","")
    return comprobar_letra(letra)

def pedir_cadena():
    cadena = input("")
    return cadena

#cuenta el número de letras de la cadena
def contar_letra(cadena: str, letra: str) -> int:
    num_letras = cadena.count(letra)
    return num_letras

def main():
    print("Introduce una frase:", end=" ")
    cadena = pedir_cadena()
    print("Introduce una letra:", end=" ")
    letra = pedir_letra()
    num_letras = contar_letra(cadena, letra)
    print (f"El número de {letra} es {num_letras}")
if __name__ == "__main__":
    main()