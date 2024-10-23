#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
from mi_libreria import comprobar_num

def comprueba_edad(num: int):
    if num < 0:
        while num < 0: 
            print ("*Error*")
            num = comprobar_num(input("Introduce una edad valida: ").replace(" ",""))
    return num

def comprueba_ingresos(num: float):
    if num < 0:
        while num < 0: 
            print ("*Error*")
            num = float(comprobar_num(input("Introduce un ingreso valido: ").replace(" ","")))
    return num
            


def main():
    edad = input("Introduce tu edad: ").replace(" ","")
    edad = comprueba_edad(comprobar_num(edad))
    if edad < 16:
        print ("Tienes",edad,"años, no tienes que tributar.")
    else: 
        ingresos = input("Introduce tus ingresos: ").replace(" ","")
        ingresos = comprueba_ingresos(float(comprobar_num(ingresos)))
        if ingresos >= 1000:
            print ("Tienes",edad,"años e ingresas",ingresos,"€ (igual o más de 1000 €), tienes que tributar.")
        else:
            print ("Tienes",edad,"años e ingresas",ingresos,"€ (menos de 1000 €), no tienes que tributar.")
    
    
if __name__ == "__main__":
    main()