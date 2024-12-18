#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
# replace para eliminar espacios
from mi_libreria import comprobar_num
# comprueba si es una edad válida, si no bucle hasta que sí. Al final retorna número.
def comprueba_edad(num: int):
    if num < 0:
        while num < 0: 
            print ("*Error*")
            num = comprobar_num(input("Introduce una edad valida: ").replace(" ",""))
    return num
  
def main():
    edad = input("Introduce la edad del cliente:").replace(" ","")
    edad = comprueba_edad(comprobar_num(edad))
    if edad < 4:# si es menor de 4 años entra gratis
       print ("Tiene",edad,"años, puede entrar gratis.")
    elif edad >= 4 and edad < 18: #Sí es de 4 a 17, paga la mitad
       print ("Tiene",edad,"años, puede entrar si pagas 5€.")
    else: # Si es mayor de edad paga el precio completo
       print ("Tiene",edad,"años, para entrar debe pagar 10€.")

if __name__ == "__main__":
    main()