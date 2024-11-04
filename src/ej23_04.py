#Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
def pedir_entero():
    try:
        entero = int(input("Introduce un número entero: "))
    except ValueError as e: # Si entero no es un int salta la excepción, y asigno ValueError a 'e'
        print("La entrada no es correcta")
        raise e  # Vuelve a lanzar la excepción capturada
    return entero


def main():
    entero = pedir_entero()
    print(entero)

if __name__ == "__main__":
    main()