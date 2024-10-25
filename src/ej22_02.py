#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
from mi_libreria import comprobar_entero
      
def pedir_edad():
    edad = input("").replace(" ","")
    return comprobar_edad(comprobar_entero(edad))
# mira si la edad no es válida
def comprobar_edad(edad):
    if edad <= 0 or edad > 125:
       while edad <= 0 or edad > 125:
           print("**ERROR** -> Introduce una edad válida:")
           edad = input("").replace(" ","")
           edad = comprobar_entero(edad)
    else:
        pass
    return edad
# guarda en una variable los años cumplidos
def obtener_anios(edad: int) -> str:
    anios = ""
    # recorre todos los números hasta su edad (desde 1)
    for i in range(1,edad+1):
            # si el ultimo año es el dado, no añade la coma
            if i == edad:
                anios += (str(i))
            else:  # de lo contario, añade la coma 
                anios += str(i) + "-"
    return anios

def main():
    print ("¿Cuál es tu edad?")
    edad = pedir_edad()
    anios = obtener_anios(edad)
    print ("Los años que ha cumplido:",anios)
if __name__ == "__main__":
    main()