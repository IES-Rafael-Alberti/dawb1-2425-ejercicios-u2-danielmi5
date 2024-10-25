#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
def pedir_cadena():
    cadena = input("Introduce una palabra: ").replace(" ","")
    return cadena
def main():
    cadena = pedir_cadena()
    # imprime la cadena y un salto de línea 10 veces
    print ((cadena+"\n")*10)

if __name__ == "__main__":
    main()