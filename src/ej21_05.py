#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def comprobar_num(num: str) -> int:
  if num.isdigit() == True:
    #Aprovecho para comprobar si el numero es positivo o negativo
    if int(num) < 0:
        while num < 0:
            print ("ERROR")
            num = int(input("Debes introducir una edad válida: ").replace(" ",""))
    if int(num) >= 0:
       return int(num)      
    return int(num)
  else:
    while num.isdigit() == False:
      print ("ERROR")
      num = input("Debes introducir una edad válida: ").replace(" ","")
      if num.isdigit() == True:
        return int(num)
    if num.isdigit():
        return int(num)
    else:
        while not num.isdigit():
            print("ERROR: Debes introducir un número: ")
            num = input("").replace(" ","")
        return int(num)

def comprueba_tributar(edad, ingresos):
    if edad >= 16:
        if ingresos >= 1000:
            print ("Tienes",edad,"años e ingresas",ingresos,"€ (igual o más de 1000 €), tienes que tributar.")
        else:
            print ("Tienes",edad,"años e ingresas",ingresos,"€ (menos de 1000 €), no tienes que tributar.")
           
    else:
       print ("Tienes",edad,"años, no tienes que tributar.")

def main():
    edad = input("Introduce tu edad: ").replace(" ","")
    edad = comprobar_num(edad)
    ingresos = input("Introduce tus ingresos: ").replace(" ","")
    ingresos = comprobar_num(ingresos)
    comprueba_tributar(edad, ingresos)
if __name__ == "__main__":
    main()