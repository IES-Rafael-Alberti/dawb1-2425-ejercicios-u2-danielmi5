#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
def comprobar_num(num: str) -> int:
  if num.isdigit() == True:   
    return int(num)
  else:
    while num.isdigit() == False:
      print ("ERROR")
      num = input("Debes introducir un número entero (positivo): ").replace(" ","")
      if num.isdigit() == True:
        return int(num)
      

def main():
    print("¿Cuál es tú edad?:")
    edad = input("").replace(" ","")
    edad = comprobar_num(edad)
    if edad >= 18:
       print ("Eres mayor de edad, puedes conducir.")
    else:
       print ("Eres menor de edad, no puedes conducir")
    
    
if __name__ == "__main__":
    main()