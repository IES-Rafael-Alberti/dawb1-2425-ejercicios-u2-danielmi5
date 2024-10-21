#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)
def validar_edad(edad):
    # como raise hace que se salga del código no hace falta poner elif
            if edad < 0:
                raise ValueError("La edad no puede ser negativa")
            if edad == 0:
                raise ValueError("La edad no puede ser 0")
            if edad > 125:
                raise ValueError("La edad no puede ser superior a 125")



def pedir_edad() -> int:
    edad = None
    while edad == None:
        try:
            edad = int(input("Introduce tu edad: "))
            validar_edad(edad)
        except ValueError:
            if edad is None:
                print("**ERROR** --> Numero equivocado, intentalo de nuevo")
                # Si salta el except la variable edad sigue valiendo None
            if edad is not None:
                print("**ERROR**  Intentalo de nuevo")
    return edad

    
def mostrar_anios(edad: int):
    for i in range(1,edad+1):
            if i == edad:
                print (i)
            else:    
                print (i, end ="-")

def main():
    edad = pedir_edad()
    if edad is not None:
        mostrar_anios(edad)
        
if __name__ == "__main__":
    main()