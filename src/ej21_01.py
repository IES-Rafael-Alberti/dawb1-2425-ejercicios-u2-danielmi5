#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

#Comprueba si la cadena es un número. Si no lo es, bucle hasta que sí. Retorna el número 
def comprobar_num(num: str) -> int:
  if num.isdigit() == True:   
    return int(num)
  else:
    while num.isdigit() == False:
      print ("ERROR")
      num = input("Debes introducir un número entero (positivo): ").replace(" ","")
      if num.isdigit() == True:
        return int(num)
# si es mayor de edad, retorna una cosa. Si no, retorna otra.
def comprobar_edad(num):
  salida = ""
  if num >= 18:
    salida = ("Eres mayor de edad, puedes conducir.")
  else:
    salida = ("Eres menor de edad, no puedes conducir.")
  return salida

def main():
    print("¿Cuál es tú edad?:")
    edad = input("").replace(" ","")
    edad = comprobar_num(edad)
    salida = comprobar_edad(edad)
    print (salida)
if __name__ == "__main__":
    main()