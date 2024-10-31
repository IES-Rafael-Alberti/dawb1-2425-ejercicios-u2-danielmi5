#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
from mi_libreria import comprobar_num, comprobar_entero
# replace para elimar espacios

# pide todos los datos necesarios, y los comprueba uno a uno (si es número y si es entero). Al final las retorna.
def pedir_datos():
    inversion = comprobar_num(input("Cantidad a invertir: ").replace(" ","")) 
    inversion = comprobar_datos(inversion)
    interes = comprobar_num(input("Interés porcentual anual (%):").replace(" ",""))
    interes = comprobar_datos(interes)
    num_años = comprobar_entero(input ("Número de años: ").replace(" ",""))
    num_años = comprobar_datos(num_años)
    return inversion, interes, num_años

#comprueba si los datos son positivos, si no, bucle hasta que sí. Al final las retorna.
def comprobar_datos(dato):
    if dato < 0:
        while dato < 0:
            print("**ERROR** -> Debes introducir un dato válido (positivo):")
            dato = input("").replace(" ","")
            dato = comprobar_num(dato)
    return dato
# calcula la cápital y la retorna
def calcula_capital(cantidad, interes, num_años):
    cantidad *= num_años + interes / 100
    return cantidad

def main():
    print ("Introduce los siguientes datos:")
    cantida_inversion, interes_anual, num_años = pedir_datos()
    print(f"El capital tras {num_años} años es:",calcula_capital(cantida_inversion, interes_anual, num_años))
if __name__ == "__main__":
    main()
