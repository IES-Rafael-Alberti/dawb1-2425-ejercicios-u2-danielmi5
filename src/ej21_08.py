#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

#Nivel	        Puntuación
#Inaceptable	0.0
#Aceptable	    0.4
#Meritorio	    0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
from mi_libreria import comprobar_num, es_decimal
# Compruebo si la puntuación está dentro del rango, si no bucle hasta que sí y retorna
def comprobar_puntuación(num):
    while num > 0 and num < 0.4 or num>0.4 and num<0.6 or num > 1 :
        print("**ERROR** -> Puntuación fuera del rango")
        num = input ("Introduce una puntuación válida: ").replace(" ","")
        num = comprobar_num(num)
    return num
    
def main():
    print ("""
Nivel	        | Puntuación
                |  
Inaceptable	| 0.0
Aceptable	| 0.4
Meritorio	| 0.6 o más (hasta 1)
""")
    puntuacion = comprobar_num(input("Introduce tu puntación: ").replace(" ",""))
    nivel = ""
    cantidad = 0
    puntuacion = comprobar_puntuación(puntuacion)
    # Dependiendo de la puntuación entra en un nivel y la cantidad que recibe es diferente.
    if puntuacion == 0.0:
        nivel = "Inaceptable"
        cantidad = 2400*puntuacion
    elif puntuacion == 0.4:
        nivel = "Aceptable"
        cantidad = 2400*puntuacion
    elif puntuacion >= 0.6:
        nivel = "Meritorio"
        cantidad = 2400*puntuacion
        
    
    print ("Tu nivel es:",nivel,)
    print ("La cantidad de dinero que recibiras es:",int(cantidad),"€")
if __name__ == "__main__":
    main()