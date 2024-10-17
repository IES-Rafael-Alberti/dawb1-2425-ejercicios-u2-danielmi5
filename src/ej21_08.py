#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

#Nivel	        Puntuación
#Inaceptable	0.0
#Aceptable	    0.4
#Meritorio	    0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
def comprobar_num(num: str) -> float:
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

def comprobar_puntuación(num):
    if not num.isdigit():
        while num.isdigit() == False:
            print("*ERROR*")
            num = input("Introduce una puntuación (número): ")
    if num.isdigit():
        num = float(num)
        if num == 0.0:
            nivel = "Inaceptable"
            cantidad = 2400*num
            return nivel, cantidad
        elif num == 0.4:
            nivel = "Aceptable"
            cantidad = 2400*num
            return nivel, cantidad
        elif num >= 0.6 and num <= 1.0:
            nivel = "Meritorio"
            cantidad = 2400*num
            return nivel, cantidad
        else: 
            print("ERROR -> Puntuación incorrecta")


    


def main():
    print ("""
Nivel	    | Puntuación
            |  
Inaceptable	| 0.0
Aceptable	| 0.4
Meritorio	| 0.6 o más

""")
    puntuacion = input("Introduce tu puntación")
    nivel, cantidad = comprobar_puntuación(puntuacion)
    print ("Tu nivel es:",nivel,)
    print ("La cantidad de dinero que recibiras es:",cantidad)

if __name__ == "__main__":
    main()