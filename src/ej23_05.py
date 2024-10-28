#Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
def pedir_contraseña():
    contraseña = input("Introduce la contraseña: ") 
    return contraseña
def comprobar_contraseña(resultado):
    contraseña = "hola"
    if contraseña != resultado:
        raise NameError ("Incorrect Password!!")
def main():
    contraseña = pedir_contraseña()
    comprobar_contraseña(contraseña)


if __name__ == "__main__":
    main()