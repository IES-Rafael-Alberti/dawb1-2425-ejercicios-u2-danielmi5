#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

#Nivel	        Puntuación
#Inaceptable	0.0
#Aceptable	    0.4
#Meritorio	    0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
from mi_libreria import comprobar_num
def comprobar_numfallido(num: str) -> float:
    con_punto == False
    if num.isdigit():
        con_punto = True
        return float(num)
    if con_punto == True:
        while num.isdigit() == False:
            punto = num.index["."]
            num2 = num.replace["."," ", 1] #Para guardar el lugar del punto
            num = num.replace[".","", 1]

            if num.isdigit() == True:
                num = num2.replace[num2[punto],"."]
            return round(float(num), 1)


    


    


    


def main():
    print ("""
Nivel	    | Puntuación
            |  
Inaceptable	| 0.0
Aceptable	| 0.4
Meritorio	| 0.6 o más

""")
    puntuacion = comprobar_num(input("Introduce tu puntación: "))
    puntuacion = float(puntuacion)
    nivel = ""
    cantidad = 0
    if puntuacion == 0.0:
        nivel = "Inaceptable"
        cantidad = 2400*num
        return nivel, cantidad
    elif puntuacion == 0.4:
        nivel = "Aceptable"
        cantidad = 2400*num
        return nivel, cantidad
    elif puntuacion >= 0.6:
        nivel = "Meritorio"
        cantidad = 2400*num
        return nivel, cantidad
    
    print ("Tu nivel es:",nivel,)
    print ("La cantidad de dinero que recibiras es:",int(cantidad),"€")

if __name__ == "__main__":
    main()