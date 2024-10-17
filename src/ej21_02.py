#Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
def comprobar_contaseña(respuesta):
    respuesta = respuesta.lower()
    contraseña = "contraseña"
    while respuesta != contraseña:
        print("Contraseña equivocada")
        respuesta = input("Intentalo de nuevo: ")
        respuesta = respuesta.lower()
    
    if respuesta == contraseña:
        print("Contraseña correcta")
    

def main():
    print("¿Cuál es la contraseña?:")
    respuesta = input("").replace(" ","")
    comprobar_contaseña(respuesta)
    
if __name__ == "__main__":
    main()