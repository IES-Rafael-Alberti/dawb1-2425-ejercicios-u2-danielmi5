#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
def comprobar_string(cadena):
    if cadena.isdigit():
        while cadena.isdigit():
            print("ERROR: Debes introducir una cadena de texto.")
            cadena = input("Introduce una cadena: ").replace(" ","")
    else:
        return cadena
    return cadena


def main():
    nombre = input("Introduce tu nombre: ").replace(" ","")
    nombre = comprobar_string(nombre)
    sexo = input("Introduce tu sexo (M/F): ").replace(" ","")
    sexo = comprobar_string(sexo)
    
    if sexo[0].upper() == "M":
        if nombre[0] > "N":
            print ("Perteneces al grupo A")
        else:
            print ("Perteneces al grupo B")
    elif sexo[0].upper() == "F":
        if nombre[0] < "M":
            print ("Perteneces al grupo A")
        else:
            print ("perteneces al grupo B")
    else:
        print("ERROR -> Sexo incorrecto")
if __name__ == "__main__":
    main()