#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
#replace para eliminar espacios
# Comprueba si es una cadena de texto, al final la retorna
def comprobar_string(cadena):
    if cadena.isdigit(): # Si es digito, bucle hasta que no
        while cadena.isdigit():
            print("ERROR: Debes introducir una cadena de texto.")
            cadena = input("Introduce una cadena: ").replace(" ","")
    
    return cadena

def main():
    nombre = input("Introduce tu nombre: ").replace(" ","")
    nombre = comprobar_string(nombre)
    sexo = input("Introduce tu sexo (M/F): ").replace(" ","")
    sexo = comprobar_string(sexo)
    
    
    if sexo[0].upper() == "M": #Si es hombre
        if nombre[0] > "N": #Si la inicial del nombre va después de la N
            print ("Perteneces al grupo A")
        else: # Si va antes
            print ("Perteneces al grupo B")
    elif sexo[0].upper() == "F": # Si es mujer
        if nombre[0] < "M": #Si la inicial del nombre va antes de la N
            print ("Perteneces al grupo A")
        else: #Si va después
            print ("perteneces al grupo B")
    else: # Si no introduce el sexo correcto, imprime un error
        print("ERROR -> Sexo incorrecto")
if __name__ == "__main__":
    main()