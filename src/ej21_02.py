#Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
# Comprueba si la respuesta es la contraseña. Retorna True si lo es y False si no
def comprobar_contraseña(respuesta: str) -> bool:
    #Transformo la respuesta en minúsculas para que coincida con la contraseña en caso de haber puesto mayúsculas
    respuesta = respuesta.lower()
    contraseña = "contraseña"
    if respuesta == contraseña:
        return True
    else: 
        return False
    

def main():
    print("¿Cuál es la contraseña?:")
    respuesta = input("").replace(" ","")
    if comprobar_contraseña(respuesta) == True: # Si es la contraseña 
        print ("Contraseña correcta")
    else: # Si no
        print("Intentos acabados, inténtelo más tarde.")
if __name__ == "__main__":
    main()