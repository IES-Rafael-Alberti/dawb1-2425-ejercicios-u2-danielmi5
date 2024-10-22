#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
# Igual que el ej 21_02, pero quitando los intentos.

def comprobar_contraseña(respuesta: str) -> bool:
    #Transformo la respuesta en minúsculas para que coincida con la contraseña en caso de haber puesto mayúsculas
    respuesta = respuesta.lower()
    contraseña = "contraseña"
    # Hasta que la respuesta no sea la contraseña no termina el bucle
    while respuesta != contraseña:
        print("Contraseña equivocada")
        respuesta = input("Intentalo de nuevo: ")
        respuesta = respuesta.lower()
    # Cuando salga del bucle devuelve True
    return True
    
    

def main():
    print("¿Cuál es la contraseña?:")
    respuesta = input("").replace(" ","") # Elimino espacios
    # Cuando termine la función imprime eso
    if comprobar_contraseña(respuesta) == True:
        print ("Contraseña correcta")
if __name__ == "__main__":
    main()
