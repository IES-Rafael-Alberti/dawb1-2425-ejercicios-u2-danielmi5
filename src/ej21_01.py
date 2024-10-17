#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
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


def comprobar_edad(edad):
    if edad >= 18:
       print ("Eres mayor de edad, puedes conducir.")
    else:
       print ("Eres menor de edad, no puedes conducir")

def main():
    print("¿Cuál es tú edad?:")
    edad = input("").replace(" ","")
    edad = comprobar_num (edad)
    comprobar_edad(edad)
if __name__ == "__main__":
    main()