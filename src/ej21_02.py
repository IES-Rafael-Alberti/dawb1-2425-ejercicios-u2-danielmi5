#Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
def comprobar_contraseña(respuesta: str) -> bool:
    #Transformo la respuesta en minúsculas para que coincida con la contraseña en caso de haber puesto mayúsculas
    respuesta = respuesta.lower()
    contraseña = "contraseña"
    intentos = 3
    while respuesta != contraseña and intentos > 0:
        print("Contraseña equivocada")
        if intentos == 1:
            # Cuando el intentos esté en el ultimo intento no quiero que haga nada, por eso el pass. 
            pass
        else:
            respuesta = input("Intentalo de nuevo: ")
        respuesta = respuesta.lower()
        intentos -= 1
    
    if respuesta == contraseña:
        return True
    else: 
        return False
    

def main():
    print("¿Cuál es la contraseña?:")
    respuesta = input("").replace(" ","")
    if comprobar_contraseña(respuesta) == True:
        print ("Contraseña correcta")
    else:
        print("Intentos acabados, inténtelo más tarde.")
if __name__ == "__main__":
    main()