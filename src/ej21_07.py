#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

##Renta:	              Tipo impositivo:
##Menos de 10000€	      5%
##Entre 10000€ y 20000€	  15%
##Entre 20000€ y 35000€	  20%
##Entre 35000€ y 60000€	  30%
##Más de 60000€	          45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
from mi_libreria import comprobar_num
def comprueba_renta(num: float):
    if num < 0:
        while num < 0: 
            print ("*Error*")
            num = float(comprobar_num(input("Introduce una renta válida: ")))
    return num
            
      
def main():
    renta = input("Introduce tu renta: ").replace(" ","")
    renta = comprueba_renta(comprobar_num(renta))
    if renta < 10000:
        print("Tu renta es de",renta,"€ y te corresponde un tipo impositivo de 5%")
    elif renta >= 10000 and renta < 20000:
        print("Tu renta es de",renta,"€ y te corresponde un tipo impositivo de 15%")
    elif renta >= 20000 and renta < 35000:
        print("Tu renta es de",renta,"€ y te corresponde un tipo impositivo de 20%")  
    elif renta >= 35000 and renta < 60000:
        print("Tu renta es de",renta,"€ y te corresponde un tipo impositivo de 30%")
    else:   
        print("Tu renta es de",renta,"€ y te corresponde un tipo impositivo de 45%")
if __name__ == "__main__":
    main()