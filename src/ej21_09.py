#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
def comprobar_num(num: str) -> int:
  if num.isdigit() == True:
    #Aprovecho para comprobar si el numero es positivo o negativo
    if int(num) < 0:
        while num < 0:
            print ("ERROR")
            num = int(input("Debes introducir un número (positivo): ").replace(" ",""))
    if int(num) >= 0:
       return int(num)      
    return int(num)
  else:
    while num.isdigit() == False:
      print ("ERROR")
      num = input("Debes introducir un número (positivo): ").replace(" ","")
      if num.isdigit() == True:
        return int(num)
    
      
def main():
    edad = input("Introduce la edad del cliente:")
    edad = comprobar_num(edad)
    if edad < 4:
       print ("Tiene",edad,"años, puede entrar gratis.")
    elif edad >= 4 and edad < 18:
       print ("Tiene",edad,"años, puede entrar si pagas 5€.")
    else:
       print ("Tiene",edad,"años, para entrar debe pagar 10€.")

if __name__ == "__main__":
    main()